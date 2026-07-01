from collections import OrderedDict


class QueryGenerator:

    DEFAULT_QUERIES = [

        "Packaging Designer",
        "Packaging Engineer",
        "Packaging Specialist",
        "Packaging Artwork Specialist",
        "Packaging Technologist",

        "Labeling Specialist",
        "Labeling Engineer",

        "Artwork Specialist",
        "Artwork Coordinator",

        "Prepress Executive",
        "Prepress Operator",

        "Production Executive",
        "Production Engineer",

        "Quality Control",
        "Quality Assurance",

        "Graphic Designer Packaging",

        "Print Production",

        "Regulatory Labeling",

        "Medical Device Packaging",

        "Pharmaceutical Packaging"

    ]

    def build(self, profile):

        queries = []

        queries.extend(
            profile.get(
                "job_titles",
                []
            )
        )

        for skill in profile.get(
            "skills",
            []
        )[:20]:

            queries.append(skill)

            queries.append(
                f"{skill} Specialist"
            )

            queries.append(
                f"{skill} Engineer"
            )

        for industry in profile.get(
            "industries",
            []
        ):

            queries.append(industry)

            queries.append(
                f"{industry} Specialist"
            )

        queries.extend(
            self.DEFAULT_QUERIES
        )

        return list(
            OrderedDict.fromkeys(

                q.strip()

                for q in queries

                if q and len(q.strip()) > 2

            )
        )[:50]