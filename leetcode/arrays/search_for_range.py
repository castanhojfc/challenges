"""
Problem:
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Solution:
Determine the first occurence that is possible to find using binary search.
Once the index is found perform two loops.
The first loop is done on the left side of the array.
The second loop is done in the remaining part.
Update the the start and end indexes accordingly.
Stop each loop when a different value is found.

Another solution is to change the binary search algorithm to ensure that the
last occurrence is always provided. We can have repeated numbers in the array.
Some times we can get the a different occurrence according to the length of
the array.
Just be sure that to check the middle element if it is already the end of
the array or if there is another element adjancent that is greater than its
value.
The solution is all about performing two searches.
The first search is done for the target itself.
The second search is done to the number lower to the target by 1.
Using this information the range can be deducted.
Special cases must be handled beforehand.

Runtimes:
Second solution:
Space: O(n)
Time: O(log(n))

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (high + low) // 2

        if nums[middle] == target:
            start = end = middle

            for number in range(middle + 1, len(nums)):
                if nums[number] == target:
                    end += 1
                else:
                    break

            for number in range(middle - 1, -1, -1):
                if nums[number] == target:
                    start -= 1
                else:
                    break

            return [start, end]

        if nums[middle] > target:
            high = middle - 1
        if nums[middle] < target:
            low = middle + 1

    return [-1, -1]


def search_range_alternative(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]

    if len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        else:
            return [-1, -1]
    end = search_last_occurrence(nums, target)

    if end == -1:
        return [-1, -1]

    for new_target in range(target - 1, -1, -1):
        start = search_last_occurrence(nums, new_target)

        if start != -1:
            return [start + 1, end]

    return [0, end]


def search_last_occurrence(array: list, element: int):
    """
    Searches for an element in a sorted array.
    Iterative approach.
    This implementation guarantees that the last occurence index is provided.
    """
    low: int = 0
    high: int = len(array) - 1

    while low <= high:
        middle: int = (low + high) // 2

        if array[middle] == element and (middle == (len(array) - 1)
                                         or array[middle + 1] > element):
            return middle
        elif array[middle] <= element:
            low = middle + 1
        else:
            high = middle - 1

    return -1


if __name__ == "__main__":
    nums1 = [5, 7, 7, 8, 8, 10]
    print(search_range_alternative(nums1, 8))

    nums2 = [1]
    print(search_range_alternative(nums2, 1))

    nums3 = []
    print(search_range_alternative(nums3, 1))

    nums4 = [1, 1, 1]
    print(search_range_alternative(nums4, 1))

    nums5 = [1, 4]
    print(search_range_alternative(nums5, 4))
