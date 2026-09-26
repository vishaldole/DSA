def binarySearch(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return -1

nums = [-1, 0, 3, 5, 9, 12, 13]
target = 5
print(f'{binarySearch(nums, target)}')
