"""
Sorting Algorithms.
"""


def bubble(arr: list[int]) -> list[int]:
    """
    Bubble Sort.

    Repeatedly compares adjacent elements and swaps them if they’re
    in the wrong order.
    How it works:
    Big elements "bubble up" to the end of the list with each pass.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    swapping: bool = True
    end: int = len(arr)
    while swapping:
        swapping = False
        for i in range(1, end):
            if arr[i - 1] > arr[i]:
                # arr[i - 1], arr[i] = arr[i], arr[i - 1]
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp
                swapping = True
        end -= 1

    return arr

    # n: int = len(arr)
    #
    # for i in range(n):
    #     for j in range(n - i - 1):
    #         # if arr[j] < arr[j + 1]:  # descending order
    #         if arr[j] > arr[j + 1]:  # ascending order
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #
    # return arr


# def insertion(arr: list[int]) -> None:
#     """
#     Insertion Sort.
#
#     Builds the final sorted list one item at a time by inserting
#     each new element into its correct position.
#     How it works: Like sorting playing cards in your hand.
#
#     Time Complexity: O()
#     Space Complexity: O()
#     """
#     pass


# def merge(arr: list[int]) -> list[int]:
#     """
#     Recursively divides the list into two halves
#     and merge with the `divide_and_conquer` function.
#
#     Time Complexity: O(nlogn)
#     Space Complexity: O(n)
#     """
#     if len(arr) < 2:
#         return arr
#
#     middle: int = len(arr) // 2
#     # left: list[int] = arr[:middle]
#     # right: list[int] = arr[middle:]
#     #
#     # return divide_and_conquer(merge(left), merge(right))
#     left: list[int] = merge(arr[:middle])
#     right: list[int] = merge(arr[middle:])
#
#     return divide_and_conquer(left, right)
#
#
# def divide_and_conquer(left: list[int], right: list[int]) -> list[int]:
#     """
#     Merge Sort.
#
#     Divides the list into halves, recursively sorts each half,
#     then merges the sorted halves together.
#     How it works: Divide-and-conquer strategy.
#
#     Time Complexity: O(n)
#     Space Complexity: O(n)
#     """
#     lst: list[int] = []
#     i, j = 0, 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             lst.append(left[i])
#             i += 1
#         else:
#             lst.append(right[j])
#             j += 1
#
#     return lst + left[i:] + right[j:]


# def quick(arr: list[int]) -> None:
#     """
#     Quick Sort.
#
#     Picks a "pivot" element, partitions the list into elements
#     less than and greater than the pivot, then sorts the parts recursively.
#     How it works: Fast in practice due to efficient partitioning.
#
#     Time Complexity: O()
#     Space Complexity: O()
#     """
#     pass
#
#
# def selection(arr: list[int]) -> None:
#     """
#     Selection Sort.
#
#     Repeatedly finds the smallest (or largest) element and moves it to
#     the beginning of the list.
#     How it works: Selects the right element and places it in the correct
#     position each time.
#
#     Time Complexity: O()
#     Space Complexity: O()
#     """
#     pass
