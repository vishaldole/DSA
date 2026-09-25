def isPowerOfTwo(n: int) -> bool:
    if n == 1:
        return True

    if n < 1 or n%2 != 0:
        return False

    return isPowerOfTwo(n/2)

num = 16
print(f'{isPowerOfTwo(num)}')
