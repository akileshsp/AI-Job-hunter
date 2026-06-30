class JobFilter:

    def __init__(self):

        self.allowed_keywords = [
            "packaging",
            "artwork",
            "label",
            "regulatory",
            "prepress",
            "graphics",
            "designer",
            "esko",
            "print",
            "pharma"
        ]

    def is_match(self, job):

        title = job.title.lower()

        for keyword in self.allowed_keywords:
            if keyword in title:
                return True

        return False