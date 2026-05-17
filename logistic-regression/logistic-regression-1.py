x = [1,2,3,4,5,6]
y = [0,0,0,1,1,1]
import math
w=0
b=0
lr=0.1
def new(w,b,n):
    return w*n+b
def s(z):
    return 1/(1+math.exp(-z))
for _ in range(500000):
    for i in range(len(x)):
        z=w*x[i]+b
        p=s(z)
        
        e=p-y[i]
        w=w-lr*e*x[i]
        b=b-lr*e
        
print(w,b)
n=float(input())
k=new(w,b,n)

print(s(k))