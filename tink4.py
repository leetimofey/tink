from math import *
def frange(x, y, jump):
    while x < y:
        yield x
        x += jump
x,y = map(float,input().split())
a=list(map(float,input().split()))
x1=sqrt((a[2]-a[0])**2+(a[3]-a[1])**2)
y1=sqrt((a[6]-a[0])**2+(a[7]-a[1])**2)
xv=a[4]-a[0]
yv=a[5]-a[1]
cosalfa=(x*xv+y*yv)/sqrt((x**2+y**2)*(xv**2+yv**2))
sinalfa=sqrt(1-cosalfa**2)
for i in frange(0, x, 0.00001):
    for j in frange(0, y, 0.00001):
        xt=i*(x1/x)
        yt=j*(y1/y)
        xt=xt*cosalfa
        yt=yt*sinalfa
        if xt+a[4]-a[0]==i and yt+a[5]-a[1]==j:
            print(i, j, end=' ')