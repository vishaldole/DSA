for i in range(3):
    for j in range(3):
        print(f'i={i} j={j}')


for i in range(3):
    for j in range(i):
        print(f'i={i} j={j}')


for i in range(5):
    for j in range(i+1):
        print(f'i={i} j={j}')

for i in range(3):
    for j in range(i,-1,-1):
        print(f'i={i} j={j}')


for i in range(5, 0, -1):
    for j in range(i):
        print(f'i={i} j={j}')