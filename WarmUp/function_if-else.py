def greet(name):
    print(f'Namaste, {name}')

greet('vishal')

def sum(a, b):
    print(f'sum of {a} and {b} is {a+b}')

sum(2, 3)

def multiply(a, b):
    print(f'multiplication of {a} and {b} is {a*b}')

multiply(10, 40)

def square(num):
    return num*num

sq = square(-3)
print(f'square value is {sq}')

z = square(99)
z = z+2
print(f'square value is {z}')


#if - else

## function to elegible to vote
def eligibleToVote(age):
    if age < 0:
        print('Invalid Input')
    elif age>=18:
        print('Eligible to vote')
    else:
        print('not eligible to vote')

eligibleToVote(18)
eligibleToVote(10)
eligibleToVote(1)
eligibleToVote(-2)

##create a function to check a number is even or odd

def evenOdd(num):
    if num%2==0:
        print('Even')
    else:
        print('Odd')

evenOdd(2)
evenOdd(100)
evenOdd(7)
evenOdd(-4)