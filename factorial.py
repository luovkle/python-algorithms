def factorial(n: int) -> int:
    """Calculate the factorial of a number.

    Args:
        n (int): Base number.

    Returns:
        int: Factorial of the base number.
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input("Number: "))
    r = factorial(n)
    print(f"Factorial: {r}")
