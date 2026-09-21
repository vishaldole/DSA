def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxOnes = 0
    cnt = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
        else:
            maxOnes = max(maxOnes, cnt)
            cnt = 0

    return max(maxOnes, cnt)

nums = [1, 1, 0, 1, 0, 1, 1, 1, 1,1]
print(f'{findMaxConsecutiveOnes(nums)}')