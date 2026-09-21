def singleNumber(nums: list[int]) -> int:
    ## Using hashMap
    # map = {}

    # for i in range(len(nums)):
    #     map[nums[i]] = map.get(nums[i], 0) + 1

    # for i in range(len(map)):
    #     if map[nums[i]] == 1:
    #         return nums[i]
    
    ## using XOR
    res = 0
    for i in range(len(nums)):
        res ^= nums[i]

    return res

nums = [4, 1, 2,1,2]
print(f'{singleNumber(nums)}')