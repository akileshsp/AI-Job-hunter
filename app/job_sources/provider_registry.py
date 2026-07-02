from app.job_sources.greenhouse_api import GreenhouseAPI
from app.job_sources.lever_api import LeverAPI
from app.job_sources.smartrecruiters_api import SmartRecruitersAPI


def get_providers():
    return [
        GreenhouseAPI(),
        LeverAPI(),
        SmartRecruitersAPI()
    ]