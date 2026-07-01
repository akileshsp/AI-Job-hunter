import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class TeamTailorAPI(BaseJobSource):

    COMPANIES = [
        # Add TeamTailor company slugs here
        # Example:
        # "axis",
        # "klarna"
    ]

    def search(self, keyword="", location=""):

        jobs = []

        keyword = keyword.lower().strip()

        for company in self.COMPANIES:

            print(f"🟢 TeamTailor :: {company}")

            try:

                response = requests.get(
                    f"https://{company}.teamtailor.com/api/jobs",
                    timeout=10,
                    headers={
                        "User-Agent": "Mozilla/5.0"
                    }
                )

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data.get("data", []):

                    attrs = item.get(
                        "attributes",
                        {}
                    )

                    title = attrs.get(
                        "title",
                        ""
                    )

                    searchable = title.lower()

                    if keyword and keyword not in searchable:
                        continue

                    jobs.append(

                        Job(

                            title=title,

                            company=company.title(),

                            location=attrs.get(
                                "location",
                                location
                            ),

                            source="TeamTailor",

                            url=attrs.get(
                                "url",
                                ""
                            ),

                            description=attrs.get(
                                "body",
                                ""
                            )

                        )

                    )

            except Exception as e:

                print(e)

        print(f"✅ TeamTailor returned {len(jobs)} jobs")

        return jobs