def moveZeroes(nums: list[int]) -> None:
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1   
        
            

    print(f'nums is {nums}')

nums = [1, 3, 0, 0, 0, 12, 14]
moveZeroes(nums)            
            