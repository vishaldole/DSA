def fun(num):
    if  num == 0:
        return 
    print(f'{num}')
    num -= 1
    fun(num)

num = 10
fun(num)


## print n to 1 using recursion

def printRecur(n):
    if n < 1:
        return 

    print(f'{n}')
    printRecur(n-1)

printRecur(13)

## print 1 to n using recursion

def printRevRecur(n):
    if n < 1:
        return 

    printRevRecur(n-1)
    print(f'{n}')
    

printRevRecur(13)

## OR 

n = 50
def printRecur(x):
    if x > n:
        return 

    print(f'{x}')
    printRecur(x+1)

printRecur(1)