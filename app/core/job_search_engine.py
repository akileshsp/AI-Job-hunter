from app.providers.aggregator import JobAggregator

from app.core.job_deduplicator import JobDeduplicator
from app.core.job_ranker import JobRanker

from app.ai.job_matcher import JobMatcher

from app.services.profile_service import ProfileService


class JobSearchEngine:

    def __init__(self, user_id=None):

        self.aggregator = JobAggregator()

        self.deduplicator = JobDeduplicator()

        self.ranker = JobRanker()

        self.matcher = JobMatcher()

        self.profile = ProfileService(
            user_id
        ).get_profile()

    def search(self, location):

        print("\n🚀 AI Job Hunter Search Started")

        jobs = self.aggregator.search(
            "",
            location
        )

        print(f"\n📥 Total Retrieved : {len(jobs)}")

        jobs = self.deduplicator.remove_duplicates(
            jobs
        )

        print(f"🧹 After Deduplication : {len(jobs)}")

        matched_jobs = []

        for job in jobs:

            matched_jobs.append(

                self.matcher.match(
                    self.profile,
                    job
                )

            )

        ranked_jobs = self.ranker.rank(
            matched_jobs
        )

        print(f"⭐ Final Ranked Jobs : {len(ranked_jobs)}")

        return ranked_jobs