def indmax(a):
    m=max(a)
    for i in range(len(a)):
        if a[i]==m:
            return i
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
b=[]
summ=0
for i in range(len(a)):
    if a[i]>=100:
        b.append(i)
        summ+=a[i]
b.reverse()
for i in range(len(b)):
    k=a[b[i]+1:]
    x=indmax(k)
    del a[b[i]+1+x]
    del a[b[i]]
for i in range(len(a)):
    summ+=a[i]
print(summ)