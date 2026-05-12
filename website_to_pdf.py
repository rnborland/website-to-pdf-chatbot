import trafilatura
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urldefrag
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from xml.sax.saxutils import escape
from datetime import datetime


START_URL = "https://example.com"
MAX_PAGES = 20

OUTPUT_FILE = f"website_knowledge_base_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

SKIP_EXTENSIONS = (
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg",
    ".pdf", ".zip", ".mp4", ".mp3", ".avi", ".mov",
    ".css", ".js", ".ico", ".xml"
)


def normalize_url(url):
    url, _ = urldefrag(url)
    return url.rstrip("/")


def same_domain(url, domain):
    parsed = urlparse(url)
    return parsed.netloc == domain


def should_skip(url):
    lower = url.lower()
    return lower.endswith(SKIP_EXTENSIONS)


def get_internal_links(url, domain):
    links = []

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"LINK FETCH FAILED: {url} - {e}")
        return links

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()

        if not href:
            continue

        full_url = normalize_url(urljoin(url, href))

        if should_skip(full_url):
            continue

        if same_domain(full_url, domain):
            links.append(full_url)

    return links


def crawl_site(start_url, max_pages):
    domain = urlparse(start_url).netloc

    visited = set()
    queue = [normalize_url(start_url)]
    crawled_urls = []

    while queue and len(crawled_urls) < max_pages:
        current_url = queue.pop(0)

        if current_url in visited:
            continue

        if should_skip(current_url):
            continue

        visited.add(current_url)
        crawled_urls.append(current_url)

        print(f"Discovered page {len(crawled_urls)}: {current_url}")

        for link in get_internal_links(current_url, domain):
            if link not in visited and link not in queue:
                queue.append(link)

    return crawled_urls


def add_text_block(story, text, style):
    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()

        if paragraph:
            story.append(Paragraph(escape(paragraph), style))
            story.append(Spacer(1, 0.12 * inch))


def main():
    urls = crawl_site(START_URL, MAX_PAGES)

    print("\nPages selected for PDF:")
    for url in urls:
        print(url)

    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54,
    )

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    heading_style = styles["Heading1"]
    body_style = styles["BodyText"]

    story = []

    story.append(Paragraph("Website Knowledge Base", title_style))
    story.append(Spacer(1, 0.25 * inch))
    story.append(Paragraph(f"Source website: {escape(START_URL)}", body_style))
    story.append(Paragraph(f"Pages crawled: {len(urls)}", body_style))
    story.append(Spacer(1, 0.25 * inch))

    for url in urls:
        print(f"\nExtracting: {url}")

        downloaded = trafilatura.fetch_url(url)

        if not downloaded:
            print(f"FAILED: {url}")
            continue

        text = trafilatura.extract(downloaded, url=url)

        if not text:
            print(f"NO TEXT FOUND: {url}")
            continue

        story.append(PageBreak())
        story.append(Paragraph(url, heading_style))
        story.append(Spacer(1, 0.15 * inch))

        add_text_block(story, text, body_style)

    doc.build(story)

    print(f"\nCreated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
