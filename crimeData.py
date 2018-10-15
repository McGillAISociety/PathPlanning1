import pandas as pd
import geopandas as gpd
import osmnx as ox
import matplotlib.pyplot as plt 

class Corner:
	def __init__(self, lat, long, name):      
		self.lat = lat
		self.long = long
		self.name = name
		self.connections = []
    
	def add_street(self, corner):	
		self.connections.append(corner)

def build_montreal():
	north = 45.512502
	south = 45.500055 
	east = -73.570142
	west = -73.583204
	G1 = ox.graph_from_bbox(north=north, south=south, east=east, west=west, network_type='walk')
	G1 = ox.project_graph(G1)
	print(G1)
	fig, ax = ox.plot_graph(G1)
	plt.imshow(fig)
	plt.show()

build_montreal()

        
      