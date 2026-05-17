x=[100,200,300,400]
y=[3,6,9,12]

w=0
b=0
lr=0.00001

for i in range(2000000):
    for j in range(len(x)):
        pred=w*x[j]+b
       
        error=pred-y[j]
        
        w=w-lr*error*x[j]
        b=b-lr*error
        
        #print(pred,"-",error,"-",w,"-",b)
        
print(w,"-",b)
print(w*500+b)
