from app.providers.base_provider import BaseProvider

from app.core.job_search_engine import JobSearchEngine

from app.ai.resume_parser import ResumeParser
from app.ai.profile_extractor import ProfileExtractor
from app.ai.profile_builder import ProfileBuilder


class RealJobProvider(BaseProvider):

    def __init__(self, user_id=None):

        self.user_id = user_id

        self.engine = JobSearchEngine(user_id)

        self.locations = [
            "Bengaluru"
        ]

        self.profile = self.load_profile()

    def load_profile(self):

        try:

            resume_path = (
                f"uploads/{self.user_id}/resume.pdf"
                if self.user_id
                else "resume/resume.pdf"
            )

            parser = ResumeParser()
            extractor = ProfileExtractor()
            builder = ProfileBuilder()

            resume_text = parser.parse(resume_path)

            profile = builder.build(
                extractor.extract(resume_text)
            )

            print("\n🤖 AI Profile")

            print(f"Name        : {profile['name']}")
            print(f"Experience  : {profile['experience']}")

            print("\n🎯 Job Titles")
            for title in profile["job_titles"][:10]:
                print(f"   • {title}")

            print("\n🛠 Tools")
            for tool in profile["tools"][:10]:
                print(f"   • {tool}")

            return profile

        except Exception as e:

            print(f"⚠ Profile generation failed : {e}")

            return None

    def search(self):

        if self.profile is None:

            return []

        jobs = []

        for location in self.locations:

            print(f"\n📍 Searching {location}")

            jobs.extend(

                self.engine.search(
                    location
                )

            )

        return jobs