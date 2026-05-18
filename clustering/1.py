import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'Age': [18, 19, 20, 21, 50, 52, 53, 55],
    'Income': [20000, 22000, 25000, 24000,
               80000, 82000, 85000, 90000]
}
df = pd.DataFrame(data)
X = df[['Age', 'Income']]
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

model = KMeans(
    n_clusters=2,
    random_state=42
)
model.fit(X_scaled)

clusters = model.labels_

df['Cluster'] = clusters

print(df)