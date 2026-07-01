import json
import requests

from app.job_sources.base_job_source import BaseJobSource
from app.models.job import Job


class GreenhouseAPI(BaseJobSource):

    BASE_URL = "https://boards-api.greenhouse.io/v1/boards"

    def __init__(self):

        with open(
            "config/companies.json",
            "r",
            encoding="utf-8"
        ) as f:

            companies = json.load(f)

        self.companies = [

            c for c in companies

            if "greenhouse" in (
                c["ats"]
                if isinstance(c["ats"], list)
                else [c["ats"]]
            )

        ]

    def search(self, keyword="", location=""):

        jobs = []

        seen = set()

        keyword = keyword.lower().strip()

        requested_location = location.lower().strip()

        for company in self.companies:

            company_name = company["company"]

            slug = company["slug"]

            print(f"🟢 Greenhouse :: {company_name}")

            try:

                response = requests.get(

                    f"{self.BASE_URL}/{slug}/jobs",

                    timeout=10

                )

                if response.status_code != 200:

                    continue

                data = response.json()

                for item in data.get("jobs", []):

                    title = item.get("title", "")

                    description = item.get(
                        "content",
                        ""
                    )

                    searchable = (
                        title + " " + description
                    ).lower()

                    if keyword:

                        if keyword not in searchable:

                            continue

                    job_location = ""

                    if isinstance(item.get("location"), dict):

                        job_location = item[
                            "location"
                        ].get(
                            "name",
                            ""
                        )

                    elif isinstance(
                        item.get("location"),
                        str
                    ):

                        job_location = item[
                            "location"
                        ]

                    if (
                        requested_location != "remote"
                        and job_location
                    ):

                        if (
                            requested_location
                            not in job_location.lower()
                            and "remote"
                            not in job_location.lower()
                        ):

                            continue

                    url = item.get(
                        "absolute_url",
                        ""
                    )

                    key = (
                        title.lower(),
                        company_name.lower(),
                        url
                    )

                    if key in seen:

                        continue

                    seen.add(key)

                    jobs.append(

                        Job(

                            title=title,

                            company=company_name,

                            location=job_location,

                            source="Greenhouse",

                            url=url,

                            description=description

                        )

                    )

            except Exception as e:

                print(e)

        print(f"✅ Greenhouse returned {len(jobs)} jobs")

        return jobs