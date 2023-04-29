from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    all_jobs = read(path)
    all_salaries = []
    for job in all_jobs:
        if job["max_salary"].isdigit():
            all_salaries.append(int(job["max_salary"]))
    return max(all_salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    all_jobs = read(path)
    all_salaries = []
    for job in all_jobs:
        if job["min_salary"].isdigit():
            all_salaries.append(int(job["min_salary"]))
    return min(all_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    # Essa função eu desenvolvi com a ajuda de um amigo, fizemos programação
    # em dupla e discutimos juntos possíveis soluções
    min_salary = job.get("min_salary")
    max_salary = job.get("max_salary")

    try:
        min = int(min_salary)
        max = int(max_salary)
        int_salary = int(salary)
    except Exception:
        raise ValueError

    if (
        min_salary is None
        or max_salary is None
        or int(min_salary) > int(max_salary)
    ):
        raise ValueError

    result = int(int_salary) >= int(min) and int(int_salary) <= int(max)

    return result


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    # Essa função eu desenvolvi com a ajuda de um amigo, fizemos programação
    # em dupla e discutimos juntos possíveis soluções
    jobs_list_filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list_filtered.append(job)
        except ValueError:
            continue

    return jobs_list_filtered
