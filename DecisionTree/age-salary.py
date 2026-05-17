from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X = [
    [22, 20000],
    [25, 25000],
    [47, 50000],
    [22, 5000]
]

y = [0, 0, 1, 0]

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42,shuffle=False)

model=DecisionTreeClassifier()
model.fit(x_train,y_train)

p=model.predict(x_test)
print(p)