from sklearn.linear_model import LinearRegression

x=[[1],[2],[3],[4]]
y=[3,6,9,12]

model=LinearRegression()

model.fit(x,y)

w=model.coef_[0]
b=model.intercept_


print("w : ",w,"\nb : ",b)
print(model.predict([[5]]))