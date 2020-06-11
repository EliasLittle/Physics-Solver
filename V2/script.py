import networkx as nx
import matplotlib.pyplot as plt
from sympy import *
from property import Property
from expression import Expression
import time

def constructGraph(props, exprs):
    G = nx.Graph()
    G.add_nodes_from([prop for prop in props])
    G.add_nodes_from([expr for expr in exprs])
    G.add_edges_from([(a,p) for a in exprs for p in a.props])
    color_map = getColorMap(G)
    return G, color_map

def getColorMap(graph):
    return [node.color for node in graph]

def solve(graph):
    for node in graph:
        if node.status == 2:
            node.solve()
    return getColorMap(graph)


if __name__ == '__main__':
    props = {
    "FRC" : None,
    "ACC" : 3,
    "MAS" : 2,
    "ARE" : None,
    "PRS" : None,
    "LEN" : None
    }

    exprs = [
    "MAS * ACC - FRC",
    "LEN * LEN - ARE",
    "PRS * ARE - FRC"
    ]

    PropObjs = {}
    for tag, val in props.items():
        x = Property(tag,value=val)
        PropObjs[tag] = x


    ExprObjs = []
    for expr in exprs:
        y = Expression(expr)
        instantiated_props = [PropObjs[str(sym)] for sym in y.vars]
        new_props = y.setProps(instantiated_props)
        PropObjs.update({new_prop.tag : new_prop for new_prop in new_props})
        ExprObjs.append(y)

    g, color_map = constructGraph(PropObjs.values(),ExprObjs)
    mapping = {n:n.name for n in g.nodes()}
    H = nx.relabel_nodes(g, mapping)
    print("Colors: "+str(color_map))
    nx.draw(H, node_color=color_map, with_labels=True, font_weight='bold')
    plt.show()

    color_map = solve(g)
    H = nx.relabel_nodes(g, mapping)
    nx.draw(H, node_color=color_map, with_labels=True, font_weight='bold')
    time.sleep(3)
    plt.show()
