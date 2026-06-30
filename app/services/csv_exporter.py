import csv
from pathlib import Path


def export_jobs(jobs):
    output_file = Path("data/jobs.csv")

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Company",
            "Job Title",
            "Location",
            "Source",
            "Match Score",
            "Apply URL"
        ])

        for job in jobs:
            writer.writerow([
                job.company,
                job.title,
                job.location,
                job.source,
                job.match_score,
                job.url
            ])

    print(f"📄 CSV Exported: {output_file}")