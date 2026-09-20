def remove_element(nums, val):
    x = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[x] = nums[i]
            x += 1
    print(f'modified array is {nums}')
    return x

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(f'number of elements not equal to val = {val} is {remove_element(nums, val)}')