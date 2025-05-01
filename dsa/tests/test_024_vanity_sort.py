"""
Test file.
"""

import pytest

from dsa_024_vanity_sort import Influencer, vanity_sort


def influencer_list(tuples: list[tuple[int, int]]) -> list[Influencer]:
    """
    Helper function to convert a list of tuples (num_selfies, num_bio_links)
    into a list of Influencer objects.
    """
    return [
        Influencer(num_selfies, num_bio_links) for num_selfies, num_bio_links in tuples
    ]


def to_tuple_list(influencers: list[Influencer]) -> list[tuple[int, int]]:
    """
    Helper function to convert back a list of Influencer objects
    into a list of (num_selfies, num_bio_links) for easy comparison.
    """
    return [
        (influencer.num_selfies, influencer.num_bio_links) for influencer in influencers
    ]


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        ([(1, 2), (10, 2)], [(1, 2), (10, 2)]),
        ([(5, 1), (0, 2)], [(5, 1), (0, 2)]),
        ([(3, 4), (12, 0), (5, 2)], [(12, 0), (5, 2), (3, 4)]),
        ([(5, 3), (10, 2), (15, 1)], [(5, 3), (10, 2), (15, 1)]),
        ([(2, 2), (4, 1), (3, 1)], [(3, 1), (4, 1), (2, 2)]),
        ([(0, 0), (0, 5), (25, 0)], [(0, 0), (0, 5), (25, 0)]),
        ([(8, 1), (1, 4), (5, 2)], [(8, 1), (5, 2), (1, 4)]),
        ([(9, 3), (4, 4), (0, 5)], [(9, 3), (4, 4), (0, 5)]),
        ([(6, 2), (12, 0), (3, 3)], [(12, 0), (6, 2), (3, 3)]),
        ([(10, 1), (5, 3), (0, 4)], [(10, 1), (5, 3), (0, 4)]),
    ],
)
def test_vanity_sort(input_data, expected_data):
    """
    Test for Vanity Sort.
    """
    influencers: list[Influencer] = influencer_list(input_data)
    expected: list[Influencer] = influencer_list(expected_data)
    result: list[Influencer] = vanity_sort(influencers)

    assert to_tuple_list(result) == to_tuple_list(expected)
