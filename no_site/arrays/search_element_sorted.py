"""
Challenge:
Search for an element in a sorted array.
Should output the index. If not found it should return -1.

Solution:
Use the binary search algorithm.

How it works:
Keep track of the lowest and highest array index.
Compute the middle index, if the element in the middle is the same return it.
Otherwise check if it is lower or higher and update the lower or higher index.
Per each iteration we are effectively narrowing the search by half.
We stop when the middle element is the same as the one we are trying to find.
Or while the lower index is not the same as the higher.

Example:
[1, 2, 2, 3, 4] key = 3

low = 0
high = 4 (length - 1)
middle = 2 (low + high) / 2

The value in the middle is lower than the key, we narrow the search by
updating the lower index to the middle + 1.

low = 3
high = 4
middle = 3

Now the middle value is the same as the element we are trying to find.

Runtimes:
Space: O(1)
Time: O(log N)
"""


def search(array: list, element: int):
    """
    Searches for an element in a sorted array.
    Iterative approach.
    """
    low: int = 0
    high: int = len(array) - 1

    while low <= high:
        middle = (low + high) // 2

        if array[middle] == element:
            return middle
        elif array[middle] < element:
            low = middle + 1
        else:
            high = middle - 1

    return -1


def search_recursive(array: list,
                     element: list,
                     low: int = None,
                     high: int = None):
    """
    Searches for an element in a sorted array.
    Recursive approach.
    """
    if not low:
        low = 0

    if not high:
        high = len(array) - 1

    while low <= high:
        middle = (low + high) // 2

        if array[middle] == element:
            return middle
        elif array[middle] < element:
            low = middle + 1
            search_recursive(array, element, low, high)
        else:
            high = middle - 1
            search_recursive(array, element, low, high)

    return -1


if __name__ == "__main__":
    key = 3
    input = [1, 2, 2, 3, 4]

    print(search_recursive(input, key))

    key = 11
    print(search_recursive(input, key))
