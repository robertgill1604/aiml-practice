from sklearn.linear_model import LogisticRegression


x = [[0],[1],[2],[3],[4],[5],[6]]
y = [0,0,0,0,1,1,1]

model=LogisticRegression()
model.fit(x,y)
w=model.coef_[0]
b=model.intercept_
print(model.predict([[7]]),model.predict_proba([[7]]))
print(model.predict([[3.4]]),model.predict_proba([[3.4]]))