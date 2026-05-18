from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from sklearn.ensemble import (
    VotingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier
)

from sklearn.metrics import accuracy_score


data = load_iris()

X = data.data
y = data.target


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# --------------------------------
# Voting Ensemble
# --------------------------------

lr = LogisticRegression(max_iter=200)

dt = DecisionTreeClassifier()

svm = SVC(probability=True)

voting_model = VotingClassifier(
    estimators=[
        ('lr', lr),
        ('dt', dt),
        ('svm', svm)
    ],
    voting='hard'
)

voting_model.fit(X_train, y_train)

voting_pred = voting_model.predict(X_test)

voting_accuracy = accuracy_score(
    y_test,
    voting_pred
)

print("Voting Accuracy :", voting_accuracy)


# --------------------------------
# Bagging - Random Forest
# --------------------------------

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_accuracy = accuracy_score(
    y_test,
    rf_pred
)

print("Random Forest Accuracy :", rf_accuracy)


# --------------------------------
# Boosting - AdaBoost
# --------------------------------

adaboost_model = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

adaboost_model.fit(X_train, y_train)

adaboost_pred = adaboost_model.predict(X_test)

adaboost_accuracy = accuracy_score(
    y_test,
    adaboost_pred
)

print("AdaBoost Accuracy :", adaboost_accuracy)