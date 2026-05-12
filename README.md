# Website-to-PDF Chatbot Builder

Convert any public website into a PDF knowledge base for AI chatbot generation.

This tool crawls a public website, extracts clean text content, and generates a combined PDF file suitable for ingestion into AI RAG/chatbot systems.

---

# Workflow

```text
Website
→ Website-to-PDF conversion
→ Upload PDF to PDF-Insights.ai
→ Generate chatbot
→ Deploy HTML chatbot
```

---

# Features

- Same-domain website crawling
- Internal link discovery
- Multi-page PDF generation
- Clean website text extraction
- Adjustable page crawl limits
- Ready for RAG/chatbot ingestion

---

# Installation

```bash
pip install -r requirements.txt
```

---

# Usage

Edit these values inside `website_to_pdf.py`:

```python
START_URL = "https://example.com"
MAX_PAGES = 20
```

Then run:

```bash
python website_to_pdf.py
```

Output:

```text
website_knowledge_base_YYYYMMDD_HHMMSS.pdf
```

---

# Generate Chatbot

After generating the PDF:

1. Upload the PDF to PDF-Insights.ai
2. Generate chatbot
3. Create embed/demo page using:

https://github.com/rnborland/HTML-chatbot-generator

---

# Related Projects

- https://pdf-insights.ai
- https://github.com/rnborland/HTML-chatbot-generator

---

# Open Source Components Used

This project builds upon several excellent open-source projects:

- Trafilatura  
  https://github.com/adbar/trafilatura

- ReportLab  
  https://www.reportlab.com/opensource/

- Beautiful Soup 4  
  https://www.crummy.com/software/BeautifulSoup/

- Requests  
  https://github.com/psf/requests

---

# License

MIT License
