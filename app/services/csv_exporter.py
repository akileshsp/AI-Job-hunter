import csv


def export_jobs(jobs):

    with open(
        "data/jobs.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Company",
            "Job Title",
            "Location",
            "AI Score",
            "Recommendation",
            "Matched Skills",
            "Source",
            "URL"
        ])

        for job in jobs:

            writer.writerow([
                job.company,
                job.title,
                job.location,
                job.match_score,
                getattr(job, "recommendation", ""),
                ", ".join(job.matched_skills),
                job.source,
                job.url
            ])

    print("\n📄 CSV Exported: data/jobs.csv")