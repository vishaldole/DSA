
def countDigit(num):

    # corner case 1, if n = 0 , then it must return 1
    if num == 0:
        return 1
    cnt = 0
    # corner case 2, if n = -641 , then it must return proper count
    num = abs(num)
    while(num):
        cnt += 1
        num //= 10

    return cnt

num = -123456787
print(f'{countDigit(num)}')