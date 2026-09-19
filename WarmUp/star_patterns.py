for i in range(4):
    for j in range(4):
        print('* ', end=' ')
    print()

for i in range(4):
    for j in range(i+1):
        print('* ', end='')
    print()

for i in range(5):
    # cnt = 0
    for j in range(i+1):
        # cnt += 1
        print(f'{j+1} ', end='')
    print()

for i in range(5):
    for j in range(i+1):
        print(f'{i+1} ', end='')
    print()

for i in range(5):
    for j in range(5 - i):
        print(f'{j+1} ', end='')
    print()

for i in range(5):
    for j in range(5 - i):
        print('* ', end='')
    print()

for i in range(5):
    #adding empty spaces
    for j in range(5 - (i+1)):
        print('  ', end='')
    #adding stars *
    for k in range(i+1):
            print(' *', end='')
    
    print()

for i in range(10):
    cnt = 1
    for j in range(i+1):
        print(f'{cnt} ', end='')
        cnt = cnt ^ 1
    print()

cnt = 1
for i in range(5):
    for j in range(i+1):
        print(f'{cnt} ', end='')
        cnt = cnt ^ 1
    print()