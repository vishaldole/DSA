def linearSearch(tar):
    for i in range(len(arr)):
        if arr[i] == tar:
            return i

    return -1

arr = [4, 9, 1, 0, 2]
tar = 1

print(f'{linearSearch(tar)}')