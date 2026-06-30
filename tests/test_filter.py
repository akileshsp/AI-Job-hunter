from app.models.job import Job
from app.search.job_filter import JobFilter

jobs = [

    Job(
        title="Senior Packaging Specialist",
        company="Pfizer",
        location="Bangalore",
        source="Test",
        url=""
    ),

    Job(
        title="Java Developer",
        company="Google",
        location="Bangalore",
        source="Test",
        url=""
    ),

    Job(
        title="Packaging Artwork Specialist",
        company="Viatris",
        location="Bangalore",
        source="Test",
        url=""
    ),

    Job(
        title="HR Recruiter",
        company="Infosys",
        location="Bangalore",
        source="Test",
        url=""
    )

]

filter_engine = JobFilter()

print("\nFiltered Jobs\n")

for job in jobs:

    if filter_engine.is_match(job):
        print("✅", job.title)

    else:
        print("❌", job.title)