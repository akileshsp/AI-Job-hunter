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

            profile = builder.build(

                extractor.extract(

                    parser.parse(resume_path)

                )

            )

            print("\n🤖 AI Profile Loaded")

            return profile

        except Exception as e:

            print(e)

            return None

    def search(self):

        if not self.profile:

            return []

        all_jobs = []

        for location in self.locations:

            print(f"\n📍 {location}")

            jobs = self.engine.search(location)

            all_jobs.extend(jobs)

        return all_jobs