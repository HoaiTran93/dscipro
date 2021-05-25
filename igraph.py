"""
DO NOT CHANGE THIS FILE
"""

class IGraph(object):
    def __init__(self):
        pass

    def vertices(self):
        raise Exception('Unimplemented yet')

    def add(self, vertex):
        raise Exception('Unimplemented yet')

    def remove(self, vertex):
        raise Exception('Unimplemented yet')

    def contain_vertex(self, vertex):
        raise Exception('Unimplemented yet')

    def contains_edge(self, from_, to_):
        raise Exception('Unimplemented yet')

    def connect(self, from_, to_, weight=0):
        raise Exception('Unimplemented yet')

    def disconnect(self, from_, to_):
        raise Exception('Unimplemented yet')

    def weight(self, from_, to_):
        raise Exception('Unimplemented yet')

    def get_outward_edges(self, from_):
        raise Exception('Unimplemented yet')

    def get_inward_edges(self, to_):
        raise Exception('Unimplemented yet')

    def size(self):
        raise Exception('Unimplemented yet')

    def in_degree(self, vertex):
        raise Exception('Unimplemented yet')

    def out_degree(self, vertex):
        raise Exception('Unimplemented yet')
