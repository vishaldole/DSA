def pallindrome(num):

    #corner case, if num is negative , then it can never be pallindrome
    if num < 0:
        return False
    new_num = 0
    old_num = num

    while num:
        rem = num % 10
        new_num = new_num * 10 + rem
        num //= 10
    
    return new_num == old_num

num = 121
print(f'{num} is pallindrome?? - {pallindrome(num)}')
    