from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Attendance': [40, 45, 50, 55, 60, 70, 75, 80, 90, 95],
    'Result': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['Hours', 'Attendance']]
y = df['Result']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
linear=SVC(kernel='linear')
linear.fit(X_train,y_train)

poly=SVC(kernel='poly')
poly.fit(X_train,y_train)

rbf=SVC(kernel='rbf')
rbf.fit(X_train,y_train)

lp=linear.predict(X_test)
pp=poly.predict(X_test)
rp=rbf.predict(X_test)

la=accuracy_score(lp,y_test)
pa=accuracy_score(pp,y_test)
ra=accuracy_score(rp,y_test)

print("Linear Kernel Accuracy :", la)
print("Polynomial Kernel Accuracy :", pa)
print("RBF Kernel Accuracy :", ra)