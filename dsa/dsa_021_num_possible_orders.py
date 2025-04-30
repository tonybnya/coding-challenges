"""
021. Number of Possible Orders.

The "factorial" of a positive integer `n`, written `n!` is the product of all
positive integers less than or equal to `n`.

`5! = 5 x 4 x 3 x 2 x 1 = 120`

The result of factorila grows even faster than exponentiation!
`n! grows faster than 2^n`

    n!  2^n
2   2   4
3   6   8
4   24  16
5   120 32
6   720 64

Influencers need to be able to schedule posts to be published in the future.
We've found that the order in which the posts are published drastically affects
their performance.

Complete the `num_possible_orders` function. It takes the number of posts an
influencer has in their backlog as input and returns the total number of
possible orders in which we could publish the posts.
"""


def num_possible_orders(num_posts: int) -> int:
    """
    Solution.
    Time Complexity: O(num_posts)
    Space Complexity: O(1)
    """
    possibities: int = 1
    for i in range(1, num_posts + 1):
        possibities *= i

    return possibities
