class JobFilter:

    def __init__(self):

        self.allowed_keywords = [

            "packaging",
            "label",
            "labeling",
            "artwork",
            "prepress",
            "repro",
            "regulatory",
            "quality",
            "print",
            "graphics",
            "graphic",
            "production",
            "pharma",
            "carton",
            "leaflet",
            "compliance",
            "packshot",
            "esko"

        ]

    def filter_jobs(self, jobs):

        filtered = []

        for job in jobs:

            text = (
                job.title +
                " " +
                getattr(job, "description", "")
            ).lower()

            if any(keyword in text for keyword in self.allowed_keywords):
                filtered.append(job)

        print(f"\n✅ Relevant Jobs : {len(filtered)} / {len(jobs)}")

        return filtered