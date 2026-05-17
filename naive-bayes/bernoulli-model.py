from sklearn.naive_bayes import BernoulliNB

X = [[1,0],[1,1],[0,0],[0,0],[1,0],[1,0]]
y = [1,1,0,0,1,1]

model=BernoulliNB()
model.fit(X,y)

print(model.predict([[0,0],[0,1],[1,0],[1,1]]))
