"""
Challenge:
Remove a given element from an array and shift the remaining elements.

Solution:
(1) Create an empty array.
(2) Go through each element of the array.
    (a) If the current element index is different from the provided position:
    copy the element.

Runtimes:
Space: O(1)
Time: O(N)
"""


def remove_element(array: list, position: int):
    """
    Removes the element in the provided position from the list.
    """
    result: list = []

    for index, element in enumerate(array):
        if index != position:
            result.append(element)

    return result


if __name__ == "__main__":
    input = [2, 3, 5, 6]

    result = remove_element(input, 1)

    print(result)
