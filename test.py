from dscipro.dgraph import *

D = DGraph()
vertices = ['B', 'E', 'A', 'M', 'J']
edges = [('B', 'A'), ('E', 'A'), ('A', 'M'), ('A', 'J')]
for v in vertices:
    D.add(v)
for (f, t) in edges:
    D.connect(f, t)

print(D)

for v in vertices:
    print('vertex:{:s}'.format(v))
    print('inward:', D.get_inward_edges(v))
    print('outward:', D.get_outward_edges(v))
    print('indegree:', D.in_degree(v))
    print('outdegree:', D.out_degree(v))

print(D.contains_edge('B', 'A'))
print(D.contains_edge('A', 'B'))
print(D.contains_edge('A', 'F'))
print(D.contains_edge('E', 'A'))

topo = TopoSort(D)
print(topo.sort())
print(D.topo())