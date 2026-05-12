Convert any public website into a PDF knowledge base for AI chatbot generation.

This tool crawls a public website, extracts clean text content, and generates a combined PDF file suitable for ingestion into AI RAG/chatbot systems.

Workflow
Website
→ Website-to-PDF conversion
→ Upload PDF to PDF-Insights.ai
→ Generate chatbot
→ Deploy HTML chatbot
Features
Same-domain website crawling
Internal link discovery
Multi-page PDF generation
Clean website text extraction
Adjustable page crawl limits
Ready for RAG/chatbot ingestion
Installation
pip install -r requirements.txt
Usage

Edit:

START_URL = "https://example.com"
MAX_PAGES = 20

Then run:

python website_to_pdf.py

Output:

website_knowledge_base_YYYYMMDD_HHMMSS.pdf
Generate Chatbot

After generating the PDF:

Upload PDF to PDF-Insights.ai
Generate chatbot
Create embed/demo page using:

HTML-chatbot-generator

Related Projects
PDF-Insights.ai
HTML-chatbot-generator
Open Source Components Used

This project builds upon several excellent open-source projects:

Trafilatura
ReportLab
Beautiful Soup 4
Requests
License

MIT License
