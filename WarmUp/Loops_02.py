#search an element and return index, if element not present then return -1.

def search(li, num):
    for i in range(len(li)):
        if(li[i] == num):
            return i
    return -1

li = [4, 2, 0, 10, 8, 30]
num = 10
res = search(li, num)

if res == -1:
    print('Element not found')
else:
    print(f'element found at {res} index')


# function that returns number of negative numbers in an array

def countNegative(li):
    cnt = 0
    for i in range(len(li)):
        if(li[i] < 0):
            cnt += 1
    return cnt

li = [2, -9, 17, -1, 1, -10, -4, 8]
print(f'negative number in li are {countNegative(li)}')

# function that return the largest numberin that array
def largestElement(li):
    max = float('-inf')
    for i in range(len(li)):
        if(li[i] > max):
            max = li[i]
    return max

li = [5, 100, 10, 8, 17, 1]

print(f'largest element in li is {largestElement(li)}')

# function that return the smallest number in that array
def smallestElement(li):
    min = float('inf')
    for i in range(len(li)):
        if(li[i] < min):
            min = li[i]
    return min

li = [-5, -100, -10, -8, -17, -1]

print(f'smallest element in li is {smallestElement(li)}')