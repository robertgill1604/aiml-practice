from sklearn.linear_model import LinearRegression
x=[[1, 2],[2, 1],[3, 3],[4, 2],[5, 5],[6, 3]]
#y = [80, 90, 140, 160, 230, 210]
y = [30*a + 10*b + 20 for a,b in x]
n1=float(input())
n2=float(input())
model=LinearRegression()

model.fit(x,y)
w1=model.coef_[0]
w2=model.coef_[1]
b=model.intercept_
print(w1,w2,b)
print(model.predict([[n1,n2]]))
print(w1*n1+w2*n2+b)