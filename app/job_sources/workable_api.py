import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class WorkableAPI(BaseJobSource):

    COMPANIES = [
        "cookunity",
        "scribbr",
        "virtuagym"
    ]

    def search(self, keyword, location):

        jobs = []

        for company in self.COMPANIES:

            print(f"🟠 Workable :: {company}")

            try:

                url = f"https://{company}.workable.com/spi/v3/jobs"

                response = requests.get(url, timeout=10)

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data.get("results", []):

                    title = item.get("title", "")

                    if keyword.lower() not in title.lower():
                        continue

                    city = ""

                    if item.get("location"):
                        city = item["location"].get("city", "")

                    jobs.append(
                        Job(
                            title=title,
                            company=company.title(),
                            location=city if city else "Remote",
                            source="Workable",
                            url=item.get("url", "")
                        )
                    )

            except Exception:
                pass

        print(f"✅ Workable returned {len(jobs)} jobs")

        return jobs