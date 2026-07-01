from app.ai.match_engine import MatchEngine
from app.database.job_repository import save_job, total_jobs
from app.providers.provider_manager import ProviderManager
from app.services.csv_exporter import export_jobs


class JobService:

    def __init__(self):

        self.provider = ProviderManager()
        self.matcher = MatchEngine()

    def run(self):

        print("\n" + "=" * 60)
        print("🚀 AI JOB HUNTER v1.0")
        print("=" * 60)

        print("\n🔍 Searching Jobs...\n")

        jobs = self.provider.search_jobs()

        print(f"\n📦 Jobs Found : {len(jobs)}")

        # AI Match
        for job in jobs:
            self.matcher.calculate_score(job)

        # Highest score first
        jobs.sort(
            key=lambda job: job.match_score,
            reverse=True
        )

        print("\n🏆 TOP MATCHES\n")

        for i, job in enumerate(jobs[:20], start=1):

            print("=" * 60)
            print(f"{i}. {job.company}")
            print(f"Role           : {job.title}")
            print(f"Location       : {job.location}")
            print(f"AI Score       : {job.match_score}%")
            print(f"Recommendation : {getattr(job, 'recommendation', '')}")
            print(f"Source         : {job.source}")
            print("=" * 60)

            save_job(job)

        export_jobs(jobs)

        print("\n📊 DATABASE")
        print(f"Total Jobs Stored : {total_jobs()}")

        print("\n✅ Backend v1.0 Completed")

        return jobs