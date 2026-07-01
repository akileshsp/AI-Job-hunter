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

        print(f"\n📥 Retrieved : {len(jobs)}")

        jobs = self.deduplicator.remove_duplicates(
            jobs
        )

        print(f"🧹 After Deduplication : {len(jobs)}")

        matched = []

        for job in jobs:

            matched.append(

                self.matcher.match(
                    self.profile,
                    job
                )

            )

        ranked = self.ranker.rank(
            matched
        )

        print(f"⭐ Ranked : {len(ranked)}")

        return ranked