def missingNumber(nums: list[int]) -> int:
    ## using total to calculate sum, and substract element from nums to find missing number
    # total = 0
    # n = len(nums)

    # for i in range(n+1):
    #     total += i

    # for i in range(n):
    #     total -= nums[i]

    # return total

    ## sum formula

    n = len(nums)
    totalSum = n * (n + 1) // 2

    return totalSum - sum(nums)

    ## using xor

    # res = len(nums)
    # for i in range(len(nums)):
    #     res ^= i
    #     res ^= nums[i]

    # return res

nums = [9,6,4,2,3,5,7,1,0]
print(f'{missingNumber(nums)}')