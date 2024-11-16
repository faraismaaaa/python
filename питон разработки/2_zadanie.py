n = int(input())
i = 1
while n >= 2**i:
    i += 1
    print((i-1), 2**(i-1))
