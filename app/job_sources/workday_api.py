import json
import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class WorkdayAPI(BaseJobSource):

    def __init__(self):

        try:

            with open("config/workday_companies.json", "r") as f:
                self.companies = json.load(f)

        except Exception:

            self.companies = []

    def search(self, keyword="", location=""):

        jobs = []

        keyword = keyword.lower()

        for company in self.companies:

            try:

                print(f"🟤 Workday :: {company['company']}")

                url = company["url"]

                response = requests.get(
                    url,
                    timeout=20,
                    headers={
                        "User-Agent": "Mozilla/5.0"
                    }
                )

                if response.status_code != 200:
                    continue

                data = response.json()

                postings = (
                    data.get("jobPostings")
                    or data.get("jobPostingsList")
                    or []
                )

                for item in postings:

                    title = item.get("title", "")

                    if keyword and keyword not in title.lower():
                        continue

                    city = ""

                    locations = item.get("locationsText")

                    if locations:
                        city = locations

                    jobs.append(

                        Job(

                            title=title,

                            company=company["company"],

                            location=city or location,

                            source="Workday",

                            url=item.get("externalPath", ""),

                            description=item.get(
                                "bulletFields",
                                ""
                            )

                        )

                    )

            except Exception as e:

                print(e)

        print(f"✅ Workday returned {len(jobs)} jobs")

        return jobs