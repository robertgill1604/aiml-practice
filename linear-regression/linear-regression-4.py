import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5, 6]    
y=[50, 80, 110, 140, 170, 200]  
w=0
b=0
lr=0.0001
for i in range(100):
    for j in range(len(x)):
        p=w*x[j]+b
        e=p-y[j]
        
        w=w-lr*e*x[j]
        b=b-lr*e

print(w,b)
n=float(input())
yn=w*n+b
print(yn)
plt.scatter(n,yn)
plt.plot(n,yn)
#plt.annotate(n, (n,yn), textcoords="offset points", xytext=(0,10), ha='center')
yp = [w*i + b for i in x]
plt.scatter(x,y)
plt.plot(x,y)
plt.plot(x,yp)
plt.scatter(x,yp)
for i in range(len(x)):
    plt.annotate(x[i], (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(x[i], (x[i], yp[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()