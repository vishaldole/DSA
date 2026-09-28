def selectionSort(nums):
    n = len(nums)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if nums[j] < nums[min]:
                min = j
        if min != i: #small improvement i.e., if min element is also the start of the loop then don't swap
            nums[i], nums[min] = nums[min], nums[i]
        print(f'array after {i+1} pass is {nums}')
    return nums

arr = [7, 1, 5, 4, 3, 2]
print(f'Finally, array becomes {selectionSort(arr)}')