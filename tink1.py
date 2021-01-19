a,b,c,d = map(int,input().split())
if d<=b:
    print(a)
else:
    sum=a+(d-b)*c
    print(sum)