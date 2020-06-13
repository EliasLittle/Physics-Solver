from property import *
from relation import *
from ExpressionTree import *
import matplotlib.pyplot as plt
import networkx as nx

print("Welcome to the Physics solver!\n")

"""
F1 = Property("frc",unit="N")
M1 = Property("mass",10,"kg")
A1 = Property("acc",2,"m/s^2")

a = Relation([M1,A1,F1],"{frc}={mass}*{acc}")

G = nx.Graph()
G.add_nodes_from([F1,M1,A1,a])
G.add_edges_from([(a,p) for p in a.props])
mapping = {n:n.getName() for n in G.nodes()}
H = nx.relabel_nodes(G, mapping)
nx.draw(H, with_labels=True, font_weight='bold')
#nx.draw_shell(G, nlist=[range(5,10),range(5)], with_labels=True, font_weight='bold')
plt.show()
"""
