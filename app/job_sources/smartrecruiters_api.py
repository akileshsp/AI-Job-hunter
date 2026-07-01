import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class SmartRecruitersAPI(BaseJobSource):

    COMPANIES = [
        "Philips",
        "Bosch",
        "Roche",
        "Danaher",
        "Eurofins"
    ]

    def search(self, keyword, location):

        jobs = []

        for company in self.COMPANIES:

            print(f"🔵 SmartRecruiters :: {company}")

            try:

                url = (
                    f"https://api.smartrecruiters.com/v1/companies/"
                    f"{company}/postings"
                )

                response = requests.get(url, timeout=10)

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data.get("content", []):

                    title = item.get("name", "")

                    if keyword.lower() not in title.lower():
                        continue

                    city = item.get("location", {}).get("city", "")

                    jobs.append(
                        Job(
                            title=title,
                            company=company,
                            location=city if city else "Remote",
                            source="SmartRecruiters",
                            url=item.get("ref", "")
                        )
                    )

            except Exception:
                pass

        print(f"✅ SmartRecruiters returned {len(jobs)} jobs")

        return jobs