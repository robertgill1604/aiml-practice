from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

t=[
    "free offer win money",
    "claim your free prize",
    "let us meet tomorrow",
    "project meeting today",
    "win cash now",
    "team lunch discussion"
]

y=[
    "spam",
    "spam",
    "ham",
    "ham",
    "spam",
    "ham"
]
v=CountVectorizer()
x=v.fit_transform(t)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,shuffle=False)
model=MultinomialNB()
model.fit(x_train,y_train)

p=model.predict(x_test)
print(p)
print(accuracy_score(p,y_test))