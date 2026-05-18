from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [
    [22, 20000],
    [25, 25000],
    [47, 50000],
    [52, 65000],
    [46, 52000],
    [56, 70000],
    [23, 22000],
    [27, 28000],
    [48, 58000],
    [50, 62000]
]

y = [0, 0, 1, 1, 1, 1, 0, 0, 1, 1]

x_train,x_test,y_train,y_test=train_test_split(
    X,y,test_size=0.3,shuffle=False
)
model=RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
model.fit(x_train,y_train)
p=model.predict(x_test)
print(p)
print(accuracy_score(p,y_test))