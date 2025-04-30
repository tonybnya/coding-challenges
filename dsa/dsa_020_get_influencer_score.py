"""
020. Get Influencer Score.

A logarithm is the inverse of an exponent.
`2^4 = 16`, so log(16) = 4 (log in base 2 because in coding we work in binary).

"log(16)" can be read as "log base 2 of 16", and means "the number of times
2 must be multiplied by itself to equal 16".

"log(16)" might also be written as `log2(16)`. So:

log2(result) = x
2 ^ x = result

Let's create an "influencer score". It will be a small number (like less than `100`)
that will influencers a metric for comparing their social media success against
their peers.

Complete the `get_influencer_score` function. An influencer score is their
engagement percentage multiplied by log base 2 of their follower count.
"""

import math


def get_influencer_score(
    average_engagement_percentage: float, num_followers: int
) -> int:
    """
    Solution.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return round(average_engagement_percentage * math.log(num_followers, 2))
