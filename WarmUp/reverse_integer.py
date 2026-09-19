def reverseInteger(num):
    sign = -1 if num < 0 else 1
    # corner case, if num is negative, then take its absolute value
    nnum = abs(num)
    rev = 0
    while(nnum):
        rem = nnum % 10
        rev = (rev * 10) + rem
        nnum //= 10

    rev = rev * sign
    # corner case, if rev is outside the signed 32-bit integer range [-2**31, (2**31) - 1], then return 0
    return 0 if (rev < -2**31 or rev > (2**31) - 1) else rev

num = 145674459
print(f'reverse of {num} is {reverseInteger(num)}') 