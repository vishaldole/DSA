def reverseString(s: list[str]) -> None:
    
    j = len(s)
    # i = 0
    # while i < j:
    #     # temp = s[i]
    #     # s[i] = s[j]
    #     # s[j] = temp
    #     s[i], s[j] = s[j], s[i]
    #     i += 1
    #     j -= 1

    for i in range(j//2):
        s[i], s[j - 1 -i] = s[j - 1 -i], s[i]
         
    print(f'reversed string in {s}')

s = ["H","a","n","n","a","h"]
reverseString(s)
    