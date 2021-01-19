n,t = map(int,input().split())
a = list(map(int,input().split()))
s = int(input())
if a[s-1]<(a[-1]/2):
    if t>=(a[s-1]-a[0]):
        print(a[-1]-a[0])
    else:
        print(a[s-1]+a[-1]-2*a[0])
else:
    if t>=(a[-1]-a[s-1]):
        print(a[-1]-a[0])
    else:
        print(2*a[-1]-a[s-1]-a[0])