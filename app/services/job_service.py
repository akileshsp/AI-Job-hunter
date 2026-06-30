from app.ai.match_engine import MatchEngine
from app.database.job_repository import save_job, total_jobs
from app.search.aggregator import SearchAggregator
from app.services.csv_exporter import export_jobs


class JobService:

    def __init__(self):
        self.search = SearchAggregator()
        self.matcher = MatchEngine()

    def run(self):
        print("\n🔍 Searching Jobs...\n")

        jobs = self.search.search_all()

        print(f"Found {len(jobs)} Jobs\n")

        for job in jobs:
            job.match_score = self.matcher.calculate_score(job.title)

            print("--------------------------------")
            print(f"Company : {job.company}")
            print(f"Role    : {job.title}")
            print(f"Location: {job.location}")
            print(f"⭐ Match : {job.match_score}%")

            save_job(job)

        export_jobs(jobs)

        print("\n📊 Database Statistics")
        print(f"Total Jobs : {total_jobs()}")

        print("\n✅ Search Completed")