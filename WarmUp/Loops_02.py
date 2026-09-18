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