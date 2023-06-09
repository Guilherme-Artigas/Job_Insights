from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    list_all_jobs = read(path)
    unique_industries = set()
    for job in list_all_jobs:
        if job["industry"] != "":
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    list_industries = []
    for i in jobs:
        if i["industry"] == industry:
            list_industries.append(i)
    return list_industries
