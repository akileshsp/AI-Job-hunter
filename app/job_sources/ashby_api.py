import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class AshbyAPI(BaseJobSource):

    COMPANIES = [
        "openai",
        "notion",
        "vercel",
        "cursor",
        "linear"
    ]

    def search(self, keyword="", location=""):

        jobs = []

        keyword = keyword.lower().strip()

        for company in self.COMPANIES:

            print(f"🟡 Ashby :: {company}")

            try:

                response = requests.get(
                    f"https://jobs.ashbyhq.com/api/non-user-graphql?organization={company}",
                    timeout=10
                )

                if response.status_code != 200:
                    continue

                data = response.json()

                postings = (
                    data.get("data", {})
                    .get("jobBoard", {})
                    .get("jobPostings", [])
                )

                for item in postings:

                    title = item.get("title", "")

                    searchable = title.lower()

                    if keyword and keyword not in searchable:
                        continue

                    jobs.append(

                        Job(

                            title=title,

                            company=company.title(),

                            location=item.get(
                                "locationName",
                                location
                            ),

                            source="Ashby",

                            url=item.get(
                                "applicationUrl",
                                ""
                            ),

                            description=""

                        )

                    )

            except Exception as e:

                print(e)

        print(f"✅ Ashby returned {len(jobs)} jobs")

        return jobs