"""
THIS FILE CONTAINS CODE for DirectedGraph (DGraph) ONLY

Students are required to complete the methods
containing phrase 'YOUR CODE HERE'
"""

from dscipro.baseimp import *


class DGraph(AbstractGraph):
    def __init__(self):
        super(DGraph, self).__init__()

    def connect(self, from_, to_, weight=0):
        # YOUR CODE HERE

        return self

    def disconnect(self, from_, to_):
        # YOUR CODE HERE

        return self

    def remove(self, vertex):
        # YOUR CODE HERE

        return self

    def topo(self):
        # YOUR CODE HERE
        # return a list of vertices sorted by topological order
        pass # done => removed

class TopoSort(object):
    def __init__(self, graph: DGraph):
        self.graph = graph

    def sort(self):
        results = []
        # YOUR CODE HERE

        return results

    def vertex2indegree(self):
        results = {}
        for v in self.graph.vertices():
            results[str(v)] = self.graph.in_degree(v)
        return results

    def list_of_zero_indegree(self):
        results = [v for v in self.graph.vertices() if self.graph.in_degree(v) == 0]
        return results
