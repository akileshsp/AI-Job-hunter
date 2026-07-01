import re
from collections import OrderedDict


class ProfileAnalyzer:

    TOOLS = [

        "Adobe Illustrator",
        "Adobe Photoshop",
        "Adobe Acrobat",
        "Esko Studio",
        "DeskPack",
        "WebCenter",
        "ArtiosCAD",
        "Global Vision",
        "TrackWise",
        "Jira",
        "SAP",
        "Power BI",
        "Excel",
        "InDesign",

        "NetApp",
        "PowerMax",
        "VMAX",
        "PowerScale",
        "Isilon",
        "OneFS",
        "Commvault",
        "Networker",
        "Dell EMC",
        "Brocade",
        "Cisco",
        "ServiceNow",
        "Linux",
        "Windows Server",
        "VMware",
        "Azure",
        "AWS"

    ]

    def analyze(self, text):

        profile = {
            "name": "",
            "experience": 0,
            "skills": [],
            "tools": [],
            "job_titles": [],
            "search_queries": []
        }

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if lines:
            profile["name"] = lines[0]

        exp = re.search(
            r"(\d+)\+?\s*years",
            text,
            re.IGNORECASE
        )

        if exp:
            profile["experience"] = int(exp.group(1))

        lower = text.lower()

        for tool in self.TOOLS:

            if tool.lower() in lower:

                profile["tools"].append(tool)

        titles = re.findall(

            r"(Senior\s+[A-Za-z&/\-\s]+|Lead\s+[A-Za-z&/\-\s]+|Principal\s+[A-Za-z&/\-\s]+|[A-Za-z&/\-\s]+Engineer|[A-Za-z&/\-\s]+Administrator|[A-Za-z&/\-\s]+Specialist|[A-Za-z&/\-\s]+Designer|[A-Za-z&/\-\s]+Analyst)",

            text,

            re.IGNORECASE

        )

        profile["job_titles"] = list(

            OrderedDict.fromkeys(

                [

                    t.strip()

                    for t in titles

                    if len(t.strip()) > 4

                ]

            )

        )

        words = re.findall(

            r"[A-Za-z][A-Za-z0-9+#./-]{3,}",

            text

        )

        stop = {

            "with",
            "have",
            "will",
            "this",
            "that",
            "years",
            "year",
            "experience",
            "experienced",
            "working",
            "senior",
            "assistant"

        }

        skills = []

        for word in words:

            if word.lower() in stop:
                continue

            skills.append(word)

        profile["skills"] = list(

            OrderedDict.fromkeys(skills)

        )[:50]

        queries = []

        queries.extend(profile["job_titles"])

        queries.extend(profile["tools"])

        queries.extend(profile["skills"])

        profile["search_queries"] = list(

            OrderedDict.fromkeys(queries)

        )[:25]

        return profile