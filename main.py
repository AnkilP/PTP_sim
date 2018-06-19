import numpy as np
import testcase
import networkx as nx

#initializng graphs
g = nx.graph()

#adding 5 camera sensors
g.add_nodes_from(nx.path_graph(5))

#adding 2 lidars
g.add_nodes_from(nx.path_graph(5))

#adding master node
g.add_nodes(11)