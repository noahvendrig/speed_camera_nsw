import pandas as pd
from scipy import spatial

df = pd.read_csv('app/cam_data.csv')

coords = df[['lat', 'lon']].values.tolist()
tree = spatial.KDTree(coords)
closest_cam = tree.query([[-33.870100, 151.094120]])
metre_dist = closest_cam[0][0]*111139 # multiply by 111139 to convert to metres

# print(closest_cam)
print(df.iloc[523])
print(metre_dist)