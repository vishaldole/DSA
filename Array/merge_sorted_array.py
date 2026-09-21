def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    ## using extra space
    # nums1copy = nums1[:m]
    # p1 = 0
    # p2 = 0
    # for i in range(m+n):
    #     if p2 >= n or p1 < m and nums1copy[p1] < nums2[p2]:
    #         nums1[i] = nums1copy[p1]
    #         p1 += 1
    #     else:
    #         nums1[i] = nums2[p2]
    #         p2 += 1

    # print(f'nums1 is {nums1}')

    p1 = m-1
    p2 = n-1

    for i in range(m+n-1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1

        else :
            nums1[i] = nums2[p2]
            p2 -= 1
    print(f'nums1 is {nums1}')

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1, 3, nums2, 3)