"""
025. Count Marketers.

Implement the `count_marketers` function. It should accept a list of strings
(job_titles) and return the number of users who've set their title to "marketer".
Lockedin users sometimes use different casing in their titles, so make sure
to account for that.
"""


def count_marketers(job_titles: list[str]) -> int:
    """
    Solution.
    Time Complexity: 0()
    Space Complexity: 0()
    """
    count: int = 0
    for job_title in job_titles:
        if job_title.strip().lower() == "marketer":
            count += 1
    return count
