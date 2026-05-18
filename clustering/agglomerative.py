from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

X = [
    [1, 2],
    [2, 3],
    [3, 4],
    [8, 8],
    [9, 9],
    [10, 10]
]

model = AgglomerativeClustering(
    n_clusters=6,
    linkage='ward'
)

labels = model.fit_predict(X)

print(labels)

for i in range(len(X)):
    plt.scatter(X[i][0], X[i][1], c=f"C{labels[i]}")

plt.show()