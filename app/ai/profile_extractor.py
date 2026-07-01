import json
import re
from collections import OrderedDict
from pathlib import Path


class ProfileExtractor:

    TOOLS = [
        "Adobe Illustrator", "Adobe Photoshop", "Adobe Acrobat",
        "Esko Studio", "DeskPack", "WebCenter", "ArtPro",
        "ArtiosCAD", "Global Vision", "TrackWise", "Jira",
        "SAP", "Power BI", "Excel", "InDesign",
        "NetApp", "Dell EMC", "PowerMax", "VMAX",
        "PowerScale", "Isilon", "OneFS",
        "Commvault", "Networker",
        "ServiceNow", "Linux", "Windows Server",
        "VMware", "Azure", "AWS",
        "Cisco", "Brocade"
    ]

    INDUSTRIES = [
        "Packaging",
        "Pharmaceutical",
        "Healthcare",
        "Medical Device",
        "Food",
        "FMCG",
        "Printing",
        "Manufacturing",
        "Information Technology",
        "Banking",
        "Automotive",
        "Retail",
        "Telecom",
        "Logistics"
    ]

    IGNORE = {
        "ABOUT",
        "PROFILE",
        "PHONE",
        "EMAIL",
        "ADDRESS",
        "TOTAL",
        "EXPERIENCE",
        "YEAR",
        "YEARS"
    }

    TITLE_PATTERNS = [

        r"Senior\s+[A-Za-z/& -]{3,40}",

        r"Lead\s+[A-Za-z/& -]{3,40}",

        r"Principal\s+[A-Za-z/& -]{3,40}",

        r"[A-Za-z/& -]+Engineer",

        r"[A-Za-z/& -]+Developer",

        r"[A-Za-z/& -]+Designer",

        r"[A-Za-z/& -]+Administrator",

        r"[A-Za-z/& -]+Consultant",

        r"[A-Za-z/& -]+Specialist",

        r"[A-Za-z/& -]+Coordinator",

        r"[A-Za-z/& -]+Executive",

        r"[A-Za-z/& -]+Analyst",

        r"[A-Za-z/& -]+Manager"

    ]

    def unique(self, values):

        cleaned = []

        for value in values:

            value = value.strip()

            if len(value) < 3:
                continue

            cleaned.append(value)

        return list(OrderedDict.fromkeys(cleaned))

    def extract(self, text):

        profile = {

            "name": "",

            "experience": 0,

            "skills": [],

            "tools": [],

            "job_titles": [],

            "industries": []

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

        for industry in self.INDUSTRIES:

            if industry.lower() in lower:

                profile["industries"].append(industry)

        titles = []

        for pattern in self.TITLE_PATTERNS:

            titles.extend(

                re.findall(

                    pattern,

                    text,

                    re.IGNORECASE

                )

            )

        profile["job_titles"] = self.unique(titles)

        words = re.findall(

            r"[A-Za-z][A-Za-z0-9+#./-]{3,}",

            text

        )

        skills = []

        for word in words:

            if word.upper() in self.IGNORE:

                continue

            if re.search(r"(.)\1{3,}", word):

                continue

            skills.append(word)

        profile["skills"] = self.unique(skills)[:60]

        profile["tools"] = self.unique(profile["tools"])

        profile["industries"] = self.unique(profile["industries"])

        Path("config").mkdir(exist_ok=True)

        with open(

            "config/profile_generated.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                profile,

                f,

                indent=4

            )

        return profile