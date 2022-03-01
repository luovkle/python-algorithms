import random
from typing import List


def linear_search(arr: List[int], x: int) -> bool:
    """Determine if a number is in a list of numbers.

    Args:
        arr (List[int]): List of numbers.
        x (int): Number to search.

    Returns:
        bool: If the number is found within the list of numbers.
    """
    for n in arr:
        if n == x:
            return True
    return False


if __name__ == "__main__":
    list_length = int(input("list length: "))
    number_to_search = int(input("number to search: "))

    elements = [random.randint(0, list_length) for i in range(list_length)]
    print(elements)

    r = linear_search(elements, number_to_search)
    print(f"{'Element found' if r else 'Element not found'}")
