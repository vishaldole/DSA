def removeDuplicate(nums):
    x = 0
    for i in range(len(nums)):
        if nums[i] > nums[x]:
            x += 1
            nums[x] = nums[i]

    print(f'modified array is {nums}')
    return x+1

nums= [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(f'it has {removeDuplicate(nums)} unique elements')