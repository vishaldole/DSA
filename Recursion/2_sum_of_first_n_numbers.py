def sumNNumbers(n):
    if n == 0:
        return 0

    return n + sumNNumbers(n-1)

n = 5
print(f'{sumNNumbers(n)}')