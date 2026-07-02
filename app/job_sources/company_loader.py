import json
from pathlib import Path


class CompanyLoader:

    def __init__(self, config_file="config/companies.json"):
        self.config_file = Path(config_file)
        self.companies = self.load()

    def load(self):
        if not self.config_file.exists():
            print(f"Config not found: {self.config_file}")
            return []

        with open(self.config_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def all(self):
        return self.companies

    def by_ats(self, ats):

        ats = ats.lower()

        return [
            company
            for company in self.companies
            if ats in [
                x.lower()
                for x in company.get("ats", [])
            ]
        ]