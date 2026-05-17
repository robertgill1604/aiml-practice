from sklearn.naive_bayes import GaussianNB

X = [
    [98,72],
    [99,75],
    [97,70],
    [103,95],
    [104,100],
    [102,90]
]

y = [
    "Healthy",
    "Healthy",
    "Healthy",
    "Sick",
    "Sick",
    "Sick"
]

model=GaussianNB()
model.fit(X,y)

p=model.predict([[110,75],[82,82]])
print(p)