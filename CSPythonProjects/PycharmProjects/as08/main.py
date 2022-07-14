class Edges(dict):
    """
    subclass of dictionary with some modifications that will also
    modify the Graph object when an Edge is created
    """

    def __init__(self, my_graph=None):
        """
        allows for graph variables to be within the scope of the edge object
        """
        super(Edges, self).__init__()
        self.my_graph = my_graph

    def __setitem__(self, key, value):
        """
        will create a blank vertex in the graph object if it is an end point
        """
        if key not in self.my_graph:
            self.my_graph.__missing__(key)
        super(Edges, self).__setitem__(key, value)

    def copy(self, new_graph=None):
        """
        makes sure that whole new edge objects are created as well when the Graph
        is copied
        """
        new = Edges(new_graph)
        if self != {}:
            for i in self:
                new[i] = self[i]
        return new


class Graph(dict):
    """
    pretty much a default dictionary except for a few modifications
    that allow for specific graph manipulation
    """

    def __missing__(self, key):
        """
        instead of creating a dictionary it creates an edge object
        with itself passed as an argument in order to give access to
        its variables
        """
        self[key] = Edges(self)
        return self[key]

    def __delitem__(self, key):
        """
        same as regular delete but it also gets rid of the ones that are keys
        in the subdictionaries (dictionaries that are values)
        """
        super(Graph, self).__delitem__(key)
        if self != {}:
            for i in self:
                if key in self[i]:
                    del self[i][key]

    def copy(self):
        """
        idk why but the default copy method was giving me an error
        so I had to re-write it and it worked fine after that
        """
        new = Graph()
        for i in self:
            new[i] = self[i].copy(new)
        return new

    def vertices(self):
        """
        shall return a set of all vertices in the graph.
        """
        return set(self.keys())

    def edges(self):
        """
        shall return a set of all edges in the graph, as 3-tuples in the form (src, dst, weight).
        """
        b = set()
        if self != {}:
            for i in self:
                if len(self[i]) > 0:
                    for j in self[i]:
                        b.add((i, j, self[i][j]))
        return b

    def adjacent(self, src, dst):
        """
        shall return whether an edge from src to dst exists.
        """
        if dst in self[src]:
            return True
        return False

    def neighbors(self, vertex):
        """
        shall return a set of all vertices adjacent to the given vertex.
        """
        if vertex in self:
            return set(self[vertex].keys())
        return set()

    def degree(self, vertex):
        """
        shall return the number of edges incident on the given vertex.
        """
        if vertex in self:
            return len(self[vertex])
        return 0

    def path_valid(self, vertices):
        """
        shall return whether a sequence of vertices is a valid path in the graph.
        """
        path = list(vertices)
        for i in range(len(path) - 1):
            if self.adjacent(path[i], path[i + 1]) is False:
                return False
        return True

    def path_length(self, vertices):
        """"
        shall return the path length of a sequence of vertices, or
        None if the path is invalid or trivial (one vertex).
        The length shall the be sum of all edge weights
        (you may assume that any_weight + any_other_weight is a valid expression).
        """
        if len(vertices) <= 1 or not self.path_valid(vertices):
            return None
        weight = self[vertices[0]][vertices[1]]
        if len(vertices) > 2:
            for i in range(1, len(vertices) - 1):
                weight += self[vertices[i]][vertices[i + 1]]
        return weight

    def is_connected(self):
        """shall return whether the graph is connected."""
        verts = self.vertices()
        for i in verts:
            verts_i = verts.copy()
            verts_i.remove(i)
            for j in verts_i:
                if self.find_path(i, j) is None:
                    return False
        return True

    def find_path(self, start_vertex, end_vertex, path=None):
        # found this on the internet https://www.python-course.eu/graphs_python.php
        """ find a path from start_vertex to end_vertex
            in graph """
        if path is None:
            path = []
        graph = self.copy()
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None


if __name__ == '__main__':
    g = Graph()
    assert len(g) == 0
    assert 'wat' not in g
    assert not g.vertices()
    edges = ('a', 'c', 8), ('a', 'd', 4), ('c', 'b', 6), ('d', 'b', 10), ('d', 'c', 2)
    for (v_from, v_to, weight) in edges:
        g[v_from][v_to] = weight
    assert len(g) == 4
    assert 'a' in g
    assert 'c' in g['a']
    assert g.vertices() == set('abcd')
    assert g.edges() == set(edges)
    assert g.degree('d') == 2 and not g.degree('b')
    assert g.adjacent('a', 'c')
    assert not g.adjacent('c', 'a')
    assert g.path_valid(('a', 'c', 'b'))
    assert not g.path_valid(('c', 'b', 'a'))
    assert not g.is_connected()
    g['b']['a'] = 1
    assert g.degree('b') == 1 and g.degree('a') == 2
    assert g.path_valid(('c', 'b', 'a'))
    assert g.path_length(('c', 'b', 'a')) == 7
    assert g.is_connected()
    del g['a']
    assert not g.is_connected()
    assert g.vertices() == set('bcd')
    assert g.degree('b') == 0

    g2 = g.copy()
    assert g2 == g
    g2['b']['e'] = 1
    assert g2 != g
    assert g2.vertices() == set('bcde')
    g2['e']['d'] = 15
    assert g2.is_connected()
    assert g2.path_length(('e', 'd', 'c', 'b')) == 23
    del g2['e']['d']
    assert g2.degree('e') == 0
    assert g2.vertices() == set('bcde')
    assert not g2.is_connected()
    g.clear()
    assert len(g) == 0
    assert len(g2) == 4