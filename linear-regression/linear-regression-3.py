from sklearn.linear_model import LinearRegression

x=[[0.5], [1.2], [2.5], [3.0], [4.5], [5.0], [6.5], [8.0]]
y=[1200, 1050, 900, 750, 700, 500, 620, 580]

model=LinearRegression()

model.fit(x,y)

w=model.coef_[0]
b=model.intercept_

print(w," ",b)
print(model.predict([[1.5]]))