from app.job_sources.greenhouse_api import GreenhouseAPI
from app.job_sources.lever_api import LeverAPI
from app.job_sources.workable_api import WorkableAPI
from app.job_sources.smartrecruiters_api import SmartRecruitersAPI
from app.job_sources.workday_api import WorkdayAPI
from app.job_sources.ashby_api import AshbyAPI
from app.job_sources.teamtailor_api import TeamTailorAPI


def get_providers():

    return [

        GreenhouseAPI(),

        LeverAPI(),

        WorkableAPI(),

        SmartRecruitersAPI(),

        WorkdayAPI(),

        AshbyAPI(),

        TeamTailorAPI()

    ]