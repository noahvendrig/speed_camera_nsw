import pandas as pd
from scipy import spatial

df = pd.read_csv('app/cam_data.csv')

coords = df[['lat', 'lon']].values.tolist()
tree = spatial.KDTree(coords)
d = tree.query([[-36.0752574, 146.9254258]])
print(d[0][0])

# for i in range(len(df)):
#     print(df['lat'][i], df['lon'][i])