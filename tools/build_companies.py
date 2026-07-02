import csv
import json
from pathlib import Path

CSV_FILE = Path("tools/companies.csv")
OUTPUT_FILE = Path("config/companies.json")


def build():

    companies = []

    with open(CSV_FILE, newline="", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            companies.append(
                {
                    "company": row["company"].strip(),
                    "slug": row["slug"].strip(),
                    "industry": row["industry"].strip(),
                    "ats": [
                        x.strip()
                        for x in row["ats"].split(",")
                        if x.strip()
                    ]
                }
            )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            companies,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(f"✅ Generated {OUTPUT_FILE}")
    print(f"✅ Companies: {len(companies)}")


if __name__ == "__main__":
    build()