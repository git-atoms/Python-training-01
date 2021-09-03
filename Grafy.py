import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

colors = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462',
          '#b3de69','#fccde5','#d9d9d9','#bc80bd','#ccebc5','#ffed6f']

G = nx.Graph()
G.add_edges_from(edges)

edges = [['x','y'],['y','z'],['z','x']]


nx.draw(G, with_labels=True)
nx.draw_networkx_edge_labels(G,edge_labels={('x','y'):'xy',\
                                            ('y','z'):'yz',\
                                            ('z','x'):'zx')}, font_color = 'red'