def merge(arr1, arr2):
    print(f'arr1 : {arr1}')
    print(f'arr2 : {arr2}')
    newMergedArray = []
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            newMergedArray.append(arr1[i])
            i += 1
        else:
            newMergedArray.append(arr2[j])
            j += 1

    # while i < m:
    #     newMergedArray.append(arr1[i])
    #     i += 1

    # while j < n:
    #     newMergedArray.append(arr2[j])
    #     j += 1

    print(f'newMergedArray: {newMergedArray + arr1[i:] + arr2[j:]}')
    return newMergedArray + arr1[i:] + arr2[j:]
    

def mergeSort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


nums = [3, 1, 2, 8]
print(f'merge sort result is {mergeSort(nums)}')
