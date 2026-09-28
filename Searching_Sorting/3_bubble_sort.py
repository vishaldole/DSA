# def bubbleSort(nums):
#     n = len(nums)

#     for i in range(n-1):
#         for j in range(n-1-i):
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#         print(f'After {i+1} iteration, we have array as {nums}')

#     return nums

# arr = [5, 4, 9, 1, 0]
# print(f'Finally, array becomes {bubbleSort(arr)}')

## IMPROVEMENT , if in any iteration there is no swapping, then stop the process. The array will be already sorted.

def bubbleSort(nums):
    n = len(nums)

    for i in range(n-1):
        isSwapped = False
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                isSwapped = True
        if isSwapped == False:
            break
        print(f'After {i+1} iteration, we have array as {nums}')

    return nums

arr = [9, 1, 2, 3]
print(f'Finally, array becomes {bubbleSort(arr)}')