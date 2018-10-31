import pandas as pd
import geopandas as gpd
import osmnx as ox
import networkx as nx
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KDTree


# Get all the crime data from the .csv file and isolate the points based on the latitudes and longtiudes
data = pd.read_csv(r'interventionscitoyendo.csv', encoding='ISO-8859-1')
inSet = data[(data.LAT <= 45.512855) & (data.LAT >= 45.502971) & (data.LONG >= -73.583204) & (data.LONG <= -73.570142)]

# Get the graph of the area which we are looking at
G = ox.graph_from_bbox(45.512855, 45.502971, -73.570142, -73.583204, network_type='walk')
fig, ax = ox.plot_graph(G,show=False, close=False)

# Convert the graph of the area into a GeoDataFrame
nodes, _ = ox.graph_to_gdfs(G)

# Create a k-d tree based on the GeoDataFrame of the map
tree = KDTree(nodes[['y', 'x']], metric='euclidean')

# Loop through all the data for the area and attributing the latitude and longtiude of each of the
# crimes to the nearest intersection node of the map
for i in range(len(inSet.LAT)):
    crime_idx = tree.query([inSet.LAT.values[i],inSet.LONG.values[i]], k=1, return_distance=False)[0]
    closest_node_to_crime = nodes.iloc[crime_idx].index.values[0]
    ax.scatter(G.node[closest_node_to_crime]['x'], G.node[closest_node_to_crime]['y'], c='red', s=3)

#Print out the graph with the compiled intersections and crime data
plt.show()
