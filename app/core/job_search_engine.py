from app.job_sources.source_manager import SourceManager
from app.core.job_deduplicator import JobDeduplicator
from app.core.job_ranker import JobRanker
from app.ai.job_matcher import JobMatcher
from app.services.profile_service import ProfileService


class JobSearchEngine:

    def __init__(self):

        self.manager = SourceManager()
        self.deduplicator = JobDeduplicator()
        self.ranker = JobRanker()
        self.matcher = JobMatcher()

        profile = ProfileService()
        self.profile = profile.get_profile()

    def search(self, keyword, location):

        jobs = self.manager.search_all(
            keyword,
            location
        )

        jobs = self.deduplicator.remove_duplicates(
            jobs
        )

        matched_jobs = []

        for job in jobs:

            matched_jobs.append(
                self.matcher.match(
                    self.profile,
                    job
                )
            )

        matched_jobs = self.ranker.rank(
            matched_jobs
        )

        return matched_jobs