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

### In these cases, return None. Only give solutions for arr size equal or greater than 2

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

print(f'second largest element is {secondLargest([6])}')

## 3. Does it handles negative elements 

### yes, it handles

## 4. Does it handles duplicate elements, i.e., for [10, 20, 20] -> it still returns 20, but ideally it should return 10

### This can be handled by giving condition that second largest can't be equal to first largest

def secondLargest(li):

    if len(li) < 2:
        return None
    l1 = float('-inf')
    l2 = float('-inf')

    for i in range(len(li)):
        if li[i] > l1:
            l2 = l1
            l1 = li[i]
        elif li[i] > l2 and li[i] != l1:
            l2 = li[i]
    
    return l2

print(f'second largest element is {secondLargest([6, 6, 1, 6])}')

## 5. what if array has only duplicates [6,6,6,6,6] -> returns -inf, it should be handled
### give condition that if l2 is -inf, return None

def secondLargest(li):

    if len(li) < 2:
        return None
    l1 = float('-inf')
    l2 = float('-inf')

    for i in range(len(li)):
        if li[i] > l1:
            l2 = l1
            l1 = li[i]
        elif li[i] > l2 and li[i] != l1:
            l2 = li[i]

    if l2 == float('-inf'):
        return None
    return l2

print(f'second largest element is {secondLargest([6, 6, 6, 6])}')