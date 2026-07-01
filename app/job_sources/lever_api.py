import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class LeverAPI(BaseJobSource):

    COMPANIES = [
        "figma",
        "canva",
        "postman",
        "miro",
        "scale-ai"
    ]

    def search(self, keyword="", location=""):

        jobs = []

        keyword = keyword.lower().strip()

        for company in self.COMPANIES:

            print(f"🟣 Lever :: {company}")

            try:

                response = requests.get(
                    f"https://api.lever.co/v0/postings/{company}?mode=json",
                    timeout=10
                )

                if response.status_code != 200:
                    continue

                for item in response.json():

                    title = item.get("text", "")

                    description = item.get(
                        "descriptionPlain",
                        ""
                    )

                    searchable = (
                        title + " " + description
                    ).lower()

                    if keyword:

                        if keyword not in searchable:

                            continue

                    jobs.append(

                        Job(

                            title=title,

                            company=company.title(),

                            location=item.get(
                                "categories",
                                {}
                            ).get(
                                "location",
                                location
                            ),

                            source="Lever",

                            url=item.get(
                                "hostedUrl",
                                ""
                            ),

                            description=description

                        )

                    )

            except Exception as e:

                print(e)

        print(f"✅ Lever returned {len(jobs)} jobs")

        return jobs