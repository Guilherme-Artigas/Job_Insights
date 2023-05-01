from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    job_mocks = [
        {
            "job_title": "Assessment Data Analyst",
            "company": "Fort Worth Independent School District",
            "state": "TX",
            "city": "Fort Worth",
            "min_salary": "19857",
            "max_salary": "38127",
            "industry": "Education",
            "rating": "3.5",
            "date_posted": "2020-05-01",
            "valid_until": "2020-06-06",
            "job_type": "FULL_TIME",
            "id": "2233",
        },
        {
            "job_title": "Commodities Quantitative Analyst - Executive",
            "company": "JPMorgan Chase &amp;amp; Co",
            "state": "TX",
            "city": "Houston",
            "min_salary": "195818",
            "max_salary": "383416",
            "industry": "Finance",
            "rating": "3.9",
            "date_posted": "2020-05-07",
            "valid_until": "2020-06-06",
            "job_type": "FULL_TIME",
            "id": "2105",
        },
        {
            "job_title": "Data Engineer, Senior with Security Clearance",
            "company": "Booz Allen Hamilton",
            "state": "VA",
            "city": "Herndon",
            "min_salary": "91443",
            "max_salary": "155868",
            "industry": "Business Services",
            "rating": "3.7",
            "date_posted": "2020-05-02",
            "valid_until": "2020-06-06",
            "job_type": "FULL_TIME",
            "id": "3323",
        },
        {
            "job_title": "Data Engineer/Architect with Security Clearance",
            "company": "Booz Allen Hamilton",
            "state": "VA",
            "city": "McLean",
            "min_salary": "74916",
            "max_salary": "128610",
            "industry": "Business Services",
            "rating": "3.7",
            "date_posted": "2020-04-24",
            "valid_until": "2020-06-06",
            "job_type": "FULL_TIME",
            "id": "3319",
        },
    ]

    sort_by(job_mocks, "min_salary")

    assert job_mocks[3]["company"] == "JPMorgan Chase &amp;amp; Co"
