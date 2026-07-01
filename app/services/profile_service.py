import json
from pathlib import Path

from app.ai.profile_analyzer import ProfileAnalyzer
from app.ai.resume_parser import ResumeParser


class ProfileService:

    def __init__(self, resume_path="resume/resume.pdf"):

        parser = ResumeParser()
        analyzer = ProfileAnalyzer()

        resume_text = parser.parse(resume_path)

        self.profile = analyzer.analyze(resume_text)

        Path("config").mkdir(exist_ok=True)

        with open(
            "config/profile_generated.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                self.profile,
                f,
                indent=4,
                ensure_ascii=False
            )

    def get_skills(self):
        return self.profile.get("skills", [])

    def get_tools(self):
        return self.profile.get("tools", [])

    def get_roles(self):
        return self.profile.get("job_titles", [])

    def get_queries(self):
        return self.profile.get("search_queries", [])

    def get_profile(self):
        return self.profile