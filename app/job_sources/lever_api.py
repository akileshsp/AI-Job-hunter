import json
import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class LeverAPI(BaseJobSource):

    def __init__(self):

        try:
            with open("config/lever_companies.json", "r") as f:
                self.companies = json.load(f)
        except Exception as e:
            print(f"❌ Failed to load lever_companies.json: {e}")
            self.companies = []

    def search(self, keyword="", location=""):

        jobs = []

        keyword = keyword.lower().strip()

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        for company in self.companies:

            slug = company["slug"]

            print(f"🟣 Lever :: {slug}")

            try:

                url = f"https://api.lever.co/v0/postings/{slug}?mode=json"

                response = requests.get(
                    url,
                    headers=headers,
                    timeout=20
                )

                if response.status_code != 200:
                    print(f"❌ {slug} -> {response.status_code}")
                    continue

                data = response.json()

                for item in data:

                    title = item.get("text", "")
                    description = item.get("descriptionPlain", "")

                    searchable = (
                        f"{title} {description}"
                    ).lower()

                    # Keyword Filter
                    if keyword:

                        words = [
                            w.strip().lower()
                            for w in keyword.split()
                            if w.strip()
                        ]

                        if words:

                            if not any(
                                word in searchable
                                for word in words
                            ):
                                continue

                    categories = item.get("categories", {})

                    jobs.append(

                        Job(

                            title=title,

                            company=company["company"],

                            location=categories.get(
                                "location",
                                location
                            ),

                            source="Lever",

                            url=item.get(
                                "hostedUrl",
                                ""
                            ),

                            description=description,

                            employment_type=categories.get(
                                "commitment",
                                ""
                            )

                        )

                    )

            except Exception as e:

                print(f"❌ {slug}: {e}")

        print(f"✅ Lever returned {len(jobs)} jobs")

        return jobs