import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_nodes_from([1,2,3])
G.add_edge(1,2)
nx.draw(G, with_labels=True, font_weight='bold')
#nx.draw_shell(G, nlist=[range(5,10),range(5)], with_labels=True, font_weight='bold')
plt.show()
