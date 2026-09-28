def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        curr = nums[i]
        prev = i-1

        while curr < nums[prev] and prev >= 0:
            nums[prev+1] = nums[prev]
            prev -= 1

        nums[prev+1] = curr
        print(f'after {i+1} insertion, array become {nums}')

    return nums

arr = [7, 4, 3, 5, 1, 2]
print(f'after complete process, array becomes {insertionSort(arr)}')