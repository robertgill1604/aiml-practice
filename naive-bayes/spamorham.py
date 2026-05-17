import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv("D:\Personal\saswinkumar17\AIML\spam1.csv")

x=data.iloc[:,:-1]
y=data.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,shuffle=False)
print(x_train)
model=BernoulliNB()

model.fit(x_train,y_train)
p=model.predict(x_test)

acc=accuracy_score(y_test,p)

print(p)
print(acc)