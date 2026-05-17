from sklearn.linear_model import LogisticRegression

X = [[40, 50],[45, 60],[50, 55],[60, 65],[65, 70],[70, 75],[80, 85]]

y = [0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print("weights:", model.coef_)
print("bias:", model.intercept_)\
    
print(model.predict([[55, 60]]))   # borderline
print(model.predict([[75, 80]]))   # strong candidate
print(model.predict([[30, 40]]))   # weak candidate

print(model.predict_proba([[55, 60]]))