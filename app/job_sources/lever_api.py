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

    def search(self, keyword, location):

        jobs = []

        for company in self.COMPANIES:

            print(f"🟣 Lever :: {company}")

            try:

                response = requests.get(
                    f"https://api.lever.co/v0/postings/{company}?mode=json",
                    timeout=20
                )

                if response.status_code != 200:
                    continue

                for item in response.json():

                    jobs.append(
                        Job(
                            title=item.get("text", ""),
                            company=company.title(),
                            location=item.get(
                                "categories",
                                {}
                            ).get(
                                "location",
                                location
                            ),
                            source="Lever",
                            url=item.get("hostedUrl", ""),
                            description=""
                        )
                    )

            except Exception as e:

                print(e)

        print(f"✅ Lever returned {len(jobs)} jobs")

        return jobs