"""
018. Get Estimated Spread.
In the social media industry, there is a concept called "spread": how much
a post spreads due to "reshares" after all the original author's followers
see it. As it turns out, social media posts spread at en exponential rate!
We've found that the estimated spread of a post can be calculated with the
formula:

`average_spread = average_audience_followers * (num_followers ^ 1.2)`

In the formula above, `average_audience_followers` is an average calculated
from each number within the `audience_followers` argument - which is a list
containing the individual follower counts of the author's followers. For example,
if `audience_followers = [2, 3, 2, 19]`, then:

- the author has 4 total followers
- each follower has their own 2, 3, 4, and 19 followers, respectively.

Complete the `get_estimated_spread()` function by implementing the formula above.
The only input is `audience_followers`, which is a list of the follower counts
of all the followers the author has. Return the estimated spread.
If the `audience_followers` list is empty return `0.0`.
"""


def get_estimated_spread(audience_followers: list[int]) -> float:
    """
    Solution.
    Time Complexity: O(num_followers)
    Space Complexity: O(1)
    """
    num_followers = len(audience_followers)
    if num_followers == 0:
        return 0.0

    avg = sum(audience_followers) / num_followers

    return avg * (num_followers**1.2)
