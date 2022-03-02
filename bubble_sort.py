import random
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Sort a list of integers in ascending order.

    Args:
        arr (List[int]): List of integers to be sorted.

    Returns:
        List[int]: Ordered list of integers.
    """
    s = n = len(arr) - 1
    for i in range(n):
        a, b = 0, 1
        for j in range(s):
            if arr[a] > arr[b]:
                arr[a], arr[b] = arr[b], arr[a]
            a, b = b, b + 1
        s -= 1
    return arr


if __name__ == "__main__":
    arr = [random.randint(0, 100) for i in range(random.randint(0, 15))]  # Example
    print(f"Original list: {arr}")
    r = bubble_sort(arr)
    print(f"Ordered list: {r}")
