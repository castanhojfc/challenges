"""
Challenge:
Remove a given element from an array and shift the remaining elements.

Solution:
(1) Create an empty array.
(2) Go through each element of the array.
    (a) If the current element index is different from the provided position:
    copy the element.

Alternative using only one array, this is a better solution because it takes
less memory.
(1) Start a counter which will point to the current index at 0.
(2) Go through each element if it is different from the value increase the
counter and copy the element. If it is different just skip.

Runtimes:
Space: O(1)
Time: O(N)

https://leetcode.com/problems/remove-element/
"""

from typing import List


def remove_element(array: list, position: int):
    """
    Removes the element in the provided position from the list.
    """
    result: list = []

    for index, element in enumerate(array):
        if index != position:
            result.append(element)

    return result


def remove_element_one_array(nums: List[int], val: int) -> int:
    """
    Removes the occurrences of the value provided.
    Returns the size of the resulting array.
    Does not use an extra array.
    """
    count = 0

    for num in nums:
        if num != val:
            nums[count] = num
            count += 1

    return count


if __name__ == "__main__":
    input = [2, 3, 5, 6]

    print(remove_element(input, 1))

    another_input = [0, 1, 2, 2, 3, 0, 4, 2]

    print(remove_element_one_array(another_input, 2))
    print(another_input)
