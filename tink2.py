n=int(input())
for i in range(9):
    if n==2**i:
        print(i)
    elif n>2**i and n<2**(i+1):
        print(i+1)