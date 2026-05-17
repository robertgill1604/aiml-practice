import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X = [
    [40, 50],
    [45, 60],
    [50, 55],
    [60, 65],
    [65, 70],
    [70, 75],
    [80, 85]
]

y = [0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[100,40],[50,90]]))

# # plot points
# for i in range(len(X)):
#     if y[i] == 0:
#         plt.scatter(X[i][0], X[i][1], marker='o')
#     else:
#         plt.scatter(X[i][0], X[i][1], marker='x')

# # decision boundary
# w1 = model.coef_[0][0]
# w2 = model.coef_[0][1]
# b = model.intercept_[0]

# x_vals = np.array([30, 90])
# y_vals = -(w1*x_vals + b)/w2

# plt.plot(x_vals, y_vals)

# plt.xlabel("Exam Score")
# plt.ylabel("Interview Score")
# plt.title("Decision Boundary")

# plt.show()