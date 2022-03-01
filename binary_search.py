from typing import List


def binary_search(arr: List[int], x: int) -> bool:
    """Checks if a number is in a list of numbers.

    Args:
        arr (List[int]): List of numbers.
        x (int): Number to search.

    Returns:
        bool: If the number is in the list.
    """
    start, end = 0, len(arr) - 1
    while True:
        middle = (start + end) // 2
        if start > end:
            return False
        if arr[middle] == x:
            return True
        elif arr[middle] > x:
            end = middle - 1
        elif arr[middle] < x:
            start = middle + 1
    return False


if __name__ == "__main__":
    arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  # Example
    x = 100  # example

    r = binary_search(arr, x)
    print(r)
