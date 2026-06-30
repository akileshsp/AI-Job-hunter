import pdfplumber
from pathlib import Path


class ResumeParser:

    def parse(self, resume_path: str):

        path = Path(resume_path)

        if not path.exists():
            raise FileNotFoundError(f"{resume_path} not found.")

        text = ""

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        print("=" * 60)
        print("📄 RESUME CONTENT")
        print("=" * 60)

        print(text[:2000])

        return textcat app/ai/resume_parser.py