## sum of all the numbers in an array
# def sumOfArray(i):

#     if i == 0:
#         return arr[0]

#     return arr[i] + sumOfArray(i-1)

# arr = [5, 3, 2, 0, 1]
# print(f'{sumOfArray(len(arr)-1)}')


## sum of all the odd numbers in an array

def sumOdd(i):

    if i == 0:
        return arr[0] if arr[0]%2==1 else 0

    if arr[i] % 2 == 1:
        return arr[i] + sumOdd(i-1)
    else:
        return sumOdd(i-1)
    
arr = [5, 2, 3, 10, 1]
print(f'{sumOdd(len(arr)-1)}')