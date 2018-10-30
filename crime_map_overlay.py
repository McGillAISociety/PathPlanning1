import pandas as pd
import geopandas as gpd
import osmnx as ox
import networkx as nx
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt

#Get all the crime data from the .csv file and isolate the points based on the latitudes and longtiudes
data = pd.read_csv(r'interventionscitoyendo.csv', encoding='ISO-8859-1')
inSet = data[(data.LAT <= 45.512855) & (data.LAT >= 45.502971) & (data.LONG >= -73.583204) & (data.LONG <= -73.570142)]

#Get the graph of the area which we are looking at
G = ox.graph_from_bbox(45.512855, 45.502971, -73.570142, -73.583204, network_type='walk')
fig, ax = ox.plot_graph(G,show=False, close=False)

#Add the points where crime has occured, based on latitudes and longitudes to the graph
ax.scatter(inSet.LONG, inSet.LAT,s=2, c='red')

#Print out the graph with the compiled intersections and crime data
plt.show()
