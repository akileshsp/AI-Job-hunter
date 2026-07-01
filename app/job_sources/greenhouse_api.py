import json
import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class GreenhouseAPI(BaseJobSource):

    BASE_URL = "https://boards-api.greenhouse.io/v1/boards"

    def __init__(self):

        with open("config/companies.json", "r") as f:

            companies = json.load(f)

        self.companies = []

        for company in companies:

            ats = company.get("ats", [])

            if isinstance(ats, str):
                ats = [ats]

            if "greenhouse" in ats:

                self.companies.append(company)

    def search(self, keyword, location):

        jobs = []
        seen = set()

        keyword = keyword.lower().strip()
        requested_location = location.lower().strip()

        for company in self.companies:

            slug = company["slug"]
            company_name = company["company"]

            print(f"🟢 Greenhouse :: {company_name}")

            url = f"{self.BASE_URL}/{slug}/jobs"

            try:

                response = requests.get(url, timeout=15)

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data.get("jobs", []):

                    title = item.get("title", "") or ""
                    description = item.get("content", "") or ""

                    searchable = f"{title} {description}".lower()

                    if keyword not in searchable:
                        continue

                    job_location = ""

                    if isinstance(item.get("location"), dict):
                        job_location = item["location"].get("name", "")
                    elif isinstance(item.get("location"), str):
                        job_location = item["location"]

                    job_location = job_location.strip()

                    if requested_location != "remote":

                        if job_location:

                            if (
                                requested_location not in job_location.lower()
                                and "remote" not in job_location.lower()
                            ):
                                continue

                    job_url = item.get("absolute_url", "")

                    unique_key = (
                        title.lower(),
                        company_name.lower(),
                        job_url
                    )

                    if unique_key in seen:
                        continue

                    seen.add(unique_key)

                    jobs.append(
                        Job(
                            title=title,
                            company=company_name,
                            location=job_location if job_location else location,
                            source="Greenhouse",
                            url=job_url,
                            description=description
                        )
                    )

            except Exception as e:

                print(f"❌ {company_name}: {e}")

        print(f"✅ Greenhouse returned {len(jobs)} jobs")

        return jobs