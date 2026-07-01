import json
from pathlib import Path

from app.ai.profile_analyzer import ProfileAnalyzer
from app.ai.resume_parser import ResumeParser


class ProfileService:

    def __init__(self, user_id=None):

        if user_id:

            resume_path = f"uploads/{user_id}/resume.pdf"

            profile_path = f"uploads/profiles/{user_id}.json"

        else:

            resume_path = "resume/resume.pdf"

            profile_path = "config/profile_generated.json"

        parser = ResumeParser()

        analyzer = ProfileAnalyzer()

        resume_text = parser.parse(resume_path)

        self.profile = analyzer.analyze(resume_text)

        Path(profile_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            profile_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.profile,
                f,
                indent=4,
                ensure_ascii=False
            )

    def get_profile(self):

        return self.profile

    def get_skills(self):

        return self.profile.get(
            "skills",
            []
        )

    def get_tools(self):

        return self.profile.get(
            "tools",
            []
        )

    def get_roles(self):

        return self.profile.get(
            "job_titles",
            []
        )

    def get_queries(self):

        return self.profile.get(
            "search_queries",
            []
        )