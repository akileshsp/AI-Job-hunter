from collections import OrderedDict


class ProfileBuilder:

    def build(self, profile):

        skills = list(OrderedDict.fromkeys(profile.get("skills", [])))
        tools = list(OrderedDict.fromkeys(profile.get("tools", [])))
        job_titles = list(OrderedDict.fromkeys(profile.get("job_titles", [])))
        industries = list(OrderedDict.fromkeys(profile.get("industries", [])))

        search_queries = []

        search_queries.extend(job_titles)
        search_queries.extend(skills)
        search_queries.extend(tools)

        search_queries = [
            q.strip()
            for q in OrderedDict.fromkeys(search_queries)
            if q and len(q.strip()) > 2
        ]

        return {
            "name": profile.get("name", ""),
            "experience": profile.get("experience", 0),
            "skills": skills,
            "tools": tools,
            "job_titles": job_titles,
            "industries": industries,
            "search_queries": search_queries
        }