from app.models.job import Job


class MockSearch:

    def search(self):

        return [

            Job(
                title="Senior Packaging Specialist",
                company="Pfizer",
                location="Bengaluru",
                source="Mock",
                url="https://example.com/job1",

                description="""
                Looking for an experienced Packaging Specialist with
                Packaging Artwork, Labeling, Esko Studio,
                Adobe Illustrator, WebCenter,
                Pharmaceutical Packaging,
                Print Production,
                Regulatory Packaging.
                """
            ),

            Job(
                title="Packaging Artwork Specialist",
                company="Viatris",
                location="Bengaluru",
                source="Mock",
                url="https://example.com/job2",

                description="""
                Candidate should have experience in
                Packaging Artwork,
                Labeling,
                Esko Studio,
                Adobe Illustrator,
                WebCenter,
                DeskPack,
                Prepress,
                Pharma Packaging,
                Print Production,
                Artwork Quality Check.
                """
            )

        ]