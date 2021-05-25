"""
THIS FILE CONTAINS CODE THAT CAN BE SHARED
for DirectedGraph (DGraph) and UndirectedGraph (UGraph)

Students are required to complete the methods
containing phrase 'YOUR CODE HERE'
"""
from dscipro.igraph import *

class VertexNode(object):
    def __init__(self, vertex):
        self.vertex = vertex
        self.in_degree_ = 0
        self.out_degree_ = 0
        self.adj_list = []

    def connect_to(self, to_, weight: float):
        # YOUR CODE HERE
        """
        guideline:
        (1) connect this node (self) to the node given in "to_"
        (2) update indegree and outdegree
        """
        pass # done => removed

    def get_outward_edges(self):
        results = []
        for edge in self.adj_list:
            results.append(edge.to_.vertex)
        return results

    def get_edge(self, to_):
        for edge in self.adj_list:
            if self.vertex == edge.from_.vertex and \
                    to_.vertex == edge.to_.vertex:
                return edge
        return None

    def remove_to(self, to_):
        # YOUR CODE HERE
        """
        guideline:
        (1) remove the edge from this node (self) to the node given in "to_"
        (2) update indegree and outdegree
        """
        pass  # done => removed

    def in_degree(self):
        return self.in_degree_

    def out_degree(self):
        return self.out_degree_

    def __str__(self):
        desc = 'V({:s}, {:d}, {:d})'.format(str(self.vertex), self.in_degree_, self.out_degree_)
        return desc

    def __eq__(self, rhs):
        if isinstance(rhs, VertexNode):
            return self.vertex == rhs.vertex
        else:
            return self.vertex == rhs  # expected: rhs is vertex data


class Edge(object):
    def __init__(self, from_: VertexNode, to_: VertexNode, weight: float = 0):
        self.from_ = from_
        self.to_ = to_
        self.weight = weight

    def __eq__(self, rhs):
        return self.from_.vertex == rhs.from_.vertex and self.to_.vertex == rhs.to_.vertex

    def __str__(self):
        desc = 'E({:s}, {:s}): {:7.2f}'.format(str(self.from_.vertex), str(self.to_.vertex), self.weight)
        return desc


#####################################################################################################################
#   AbstractGraph: implements all the methods in IGraph that are common for directed- and undirected-graph
#   directed-graph (DGraph): inherits AbstractGraph and add the implementation specific for directed-grap
#   undirected-graph (UGraph): inherits AbstractGraph and add the implementation specific for undirected-grap
#####################################################################################################################
class AbstractGraph(IGraph):
    def __init__(self):
        super(AbstractGraph, self).__init__()
        self.node_list = []  # store all vertex nodes in the graph

    """
    Protected section:
    contains utilities that support the implementation of public methods
    """
    def _get_vertex_node(self, vertex):
        for node in self.node_list:
            if node.vertex == vertex:
                return node
        return None

    def _force_node_contained(self, vertex):
        node = self._get_vertex_node(vertex)
        if node is None:
            msg = 'Node: "{:s}"  is not exist'.format(str(vertex))
            raise Exception(msg)
        return node

    def _force_edge_contained(self, from_, to_):
        node_from = self._force_node_contained(from_)
        node_to = self._force_node_contained(to_)
        edge = node_from.get_edge(node_to)
        if edge is None:
            msg = 'Edge: "{:s} -> {:s}" is not exist'.format(str(from_), str(to_))
            raise Exception(msg)
        return edge, node_from, node_to

    """
    Public section:
    The methods in this section can be shared by UGraph and DGraph
    """
    def vertices(self):
        # YOUR CODE HERE
        # return a list of vertices
        pass # done => removed

    def add(self, vertex):
        # YOUR CODE HERE
        pass  # done => removed

    def contain_vertex(self, vertex):
        # YOUR CODE HERE
        pass  # done => removed

    def contains_edge(self, from_, to_):
        # YOUR CODE HERE
        pass  # done => removed

    def weight(self, from_, to_):
        # YOUR CODE HERE
        pass  # done => removed

    def get_outward_edges(self, from_):
        # YOUR CODE HERE
        pass  # done => removed

    def get_inward_edges(self, to_):
        # YOUR CODE HERE
        pass  # done => removed

    def size(self):
        # YOUR CODE HERE
        pass  # done => removed

    def in_degree(self, vertex):
        # YOUR CODE HERE
        pass  # done => removed

    def out_degree(self, vertex):
        # YOUR CODE HERE
        pass  # done => removed

    def __str__(self):
        desc = '#' * 80 + '\n'
        desc += 'Vertices:\n'
        desc += '-' * 40 + '\n'
        for node in self.node_list:
            desc += str(node) + '\n'
        desc += '\n'
        desc += 'Edges:\n'
        desc += '-' * 40 + '\n'
        for nodeF in self.node_list:
            for edge in nodeF.adj_list:
                desc += str(edge) + '\n'
        desc += '#' * 80 + '\n'
        return desc

    """
    Public section:
    The methods in this sections will be overridden in subclasses: DGraph and UGraph
    """
    def connect(self, from_, to_, weight=0):
        raise Exception('Unimplemented yet')

    def disconnect(self, from_, to_):
        raise Exception('Unimplemented yet')

    def remove(self, vertex):
        raise Exception('Unimplemented yet')