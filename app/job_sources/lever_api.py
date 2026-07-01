import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class LeverAPI(BaseJobSource):

    def __init__(self):

        self.companies = [
            "figma",
            "canva",
            "postman",
            "miro",
            "scale-ai"
        ]

    def search(self, keyword, location):

        jobs = []

        search_terms = [
            "packaging",
            "artwork",
            "label",
            "labeling",
            "prepress",
            "print",
            "quality"
        ]

        for company in self.companies:

            print(f"🟣 Lever :: {company}")

            url = f"https://api.lever.co/v0/postings/{company}?mode=json"

            try:

                response = requests.get(url, timeout=15)

                if response.status_code != 200:
                    continue

                data = response.json()

                for item in data:

                    title = item.get("text", "")
                    content = title.lower()

                    if not any(term in content for term in search_terms):
                        continue

                    jobs.append(
                        Job(
                            title=title,
                            company=company.title(),
                            location=item.get("categories", {}).get(
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