for i in range(2, 9, 2):
    print(f'hello world {i}')


for i in range(5, 0, -1):
    print(f'hello world {i}')

for i in range(5, 0):
    print(f'hello world {i}')

for i in range(1, 0, -1):
    print(f'hello world {i}')

def greet(i):
    print(f'namaste {i}')

for i in range(10):
    greet(i)

# accessing arrays
li = [10, 5, 7, 0, 8, 3, 88]
print(f'length of array {li} is {len(li)}')

for i in range(len(li)):
    print(f'element at {i} in li is {li[i]}')

#print all the even numbers from array li

for i in range(len(li)):
    if li[i] % 2 == 0:
        print(li[i])


# while loop

i = 0
while i < 5:
    print(f'i is {i}')
    i += 1
