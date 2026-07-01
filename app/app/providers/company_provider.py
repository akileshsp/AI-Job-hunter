import json

from app.providers.base_provider import BaseProvider
from app.models.job import Job


class CompanyProvider(BaseProvider):

    def __init__(self):

        with open("config/companies.json", "r") as f:
            data = json.load(f)

        self.companies = data["companies"]

    def search(self):

        jobs = []

        print("\n🏢 Searching Company Career Pages...\n")

        for company in self.companies:

            print(f"🔍 {company}")

            # Placeholder
            # Next we'll replace this with real company career page search.

            jobs.append(
                Job(
                    title="Packaging Specialist",
                    company=company,
                    location="Bengaluru",
                    source="Company Career",
                    url="",
                    description="Packaging Artwork Labeling Esko Studio Adobe Illustrator"
                )
            )

        return jobs