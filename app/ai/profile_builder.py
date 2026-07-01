from collections import OrderedDict

from app.ai.query_generator import QueryGenerator


class ProfileBuilder:

    MAX_JOB_TITLES = 10
    MAX_SKILLS = 15
    MAX_TOOLS = 10
    MAX_INDUSTRIES = 5

    def __init__(self):

        self.generator = QueryGenerator()

    def unique(self, values):

        cleaned = []

        for value in values:

            if not value:
                continue

            value = value.strip()

            if len(value) < 3:
                continue

            cleaned.append(value)

        return list(
            OrderedDict.fromkeys(cleaned)
        )

    def build(self, profile):

        job_titles = self.unique(
            profile.get("job_titles", [])
        )[:self.MAX_JOB_TITLES]

        skills = self.unique(
            profile.get("skills", [])
        )[:self.MAX_SKILLS]

        tools = self.unique(
            profile.get("tools", [])
        )[:self.MAX_TOOLS]

        industries = self.unique(
            profile.get("industries", [])
        )[:self.MAX_INDUSTRIES]

        profile = {

            "name": profile.get(
                "name",
                ""
            ),

            "experience": profile.get(
                "experience",
                0
            ),

            "skills": skills,

            "tools": tools,

            "job_titles": job_titles,

            "industries": industries

        }

        profile["search_queries"] = (
            self.generator.build(profile)
        )

        return profile