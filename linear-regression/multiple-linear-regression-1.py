x=[[1, 2],[2, 1],[3, 3],[4, 2],[5, 5],[6, 3]]
y = [80, 90, 140, 160, 230, 210]

n1=float(input())
n2=float(input())

w1=0
w2=0
b=0
lr=0.01
for _ in range(5000):
    for i in range(len(x)):
        p=w1*x[i][0]+w2*x[i][1]+b
        e=p-y[i]
        
        w1=w1-lr*e*x[i][0]
        w2=w2-lr*e*x[i][1]
        b=b-lr*e        
        
print(w1,w2,b)
print(w1*n1+w2*n2+b)
