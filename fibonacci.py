import random
from typing import List


def fibonacci(n: int) -> List[int]:
    """Generates a list of all fibonacci numbers that are equal to or smaller
    than one number.

    Args:
        n (int): Limit.

    Returns:
        List[int]: List of fibonacci numbers.
    """
    arr = []
    a, b = 0, 1
    while b <= n:
        arr.append(b)
        a, b = b, a + b
    return arr


if __name__ == "__main__":
    arr = fibonacci(random.randint(1, 100))
    print(arr)
