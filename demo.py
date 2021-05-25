from dscipro.dgraph import *

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'C'), ('F', 'C')]

graph = DGraph()
for v in vertices:
    graph.add(v)
for (f, t) in edges:
    graph.connect(f, t)

topo = graph.topo()
print(topo)
