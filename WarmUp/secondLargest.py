def secondLargest(li):
    l1 = float('-inf')
    l2 = float('-inf')

    for i in range(len(li)):
        if li[i] > l1:
            l2 = l1
            l1 = li[i]
        elif li[i] > l2:
            l2 = li[i]

    return l2

print(f'second largest element is {secondLargest([ 4, 1 ])}')

# considering corner cases
## 1. what if array is null
## 2. what if array has only one element

### In these cases, return null. Only give solutions for arr size equal or greater than 2

def secondLargest(li):

    if len(li) < 2:
        return None
    l1 = float('-inf')
    l2 = float('-inf')

    for i in range(len(li)):
        if li[i] > l1:
            l2 = l1
            l1 = li[i]
        elif li[i] > l2:
            l2 = li[i]

    return l2

print(f'second largest element is {secondLargest([6, 6, 5, 4])}')