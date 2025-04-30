"""
019. Get Follower Prediction.
While the influencers who use our platform are really great at taking selfies,
most aren't super great at math. We need to write a tool that predicts an
influencer's follower growth over time.

A Geometric Sequence is a sequence in which the next number is obtaining by
multiplying the current one by a fixed multiplier. Example:
100 - 200 - 400 - 800 - 1600
Here, the multiplier is 2.
The mathematic formula for this sequence is:

`An = A1 * r^(n - 1)`

Where:
- `An` (A sub n) is the n-th term
- `A1` (A sub 1) is the first term
- `r` is the common ratio (the multiplier)
- `n` is the term number (like the fourth number or the sixth number...)

Complete the 'get_follower_prediction()' function.
- `"fitness" influencers`: follower count `quadruples` each month
- `"cosmetic" influencers`: follower count `triples` each month
- `All other influencers`: follower count `doubles` each month

For example, if a fitness influencer starts with `10` followers, then after
`1` month they should have `40` followers. After `2` months, they should have
`160` followers; etc.

Use a geometric sequence formula that's slightly modified for this problem:
`total = a1 * r^n`
"""


def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:
    """
    Solution.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    factor = 2
    match influencer_type:
        case "fitness":
            factor = 4
        case "cosmetic":
            factor = 3

    return follower_count * (factor**num_months)
