"""
Dictionary representation of Graph
"""

class Edges(dict):

        def __init__(self, graph=None):
	        self.graph = graph

	    def __delitem__(self, key):
       super(Edges, self).__delitem__(key)

    def __setitem__(self, key, value):
    14	        if self.graph != None:
    15	            if key not in self.graph:
    16	                self.graph.__missing__(key)
    17
    18	        super(Edges, self).__setitem__(key, value)
    19
    20	    def copy(self, graph=None):
    21	        edge_graph = Edges()
    22	        edge_graph.graph = graph
    23	        if self != {}:
    24	            for w in self:
    25	                edge_graph[w]= self[w]
    26	        return edge_graph
    27
    28
    29	class Graph(dict):
    30	    " Graph class"
    31
    32	    def __missing__(self, key):
    33	        self[key] = Edges(graph=self)
    34	        return self[key]
    35
    36	    def __delitem__(self, key):
    37	        self.pop(key)
    38	        for a in self:
    39	            if self[a]!={}:
    40	                if key in self[a]:
    41	                    self[a].pop(key)
    42
    43	    def __len__(self):
    44	        return len(self.keys())
    45
    46	    def copy(self):
    47	        copy_graph = Graph()
    48	        for i in self:
    49	            copy_graph[i] = self[i].copy(graph = copy_graph)
    50
    51	        return copy_graph
    52
    53	    def vertices(self):
    54	        return set(self.keys())
    55
    56	    def edges(self):
    57	        list_edges = []
    58	        for q in self:
    59	            if self[q] != {}:
    60	                # start = q
    61	                # destination = self[q].keys()
    62	                # weight = self[q].values()
    63	                for i in self[q].keys():
    64	                    a = (q, i, self[q][i])
    65	                    list_edges.append(a)
    66
    67	        if len(list_edges) != 0:
    68	            Edge = {list_edges[0]}
    69	        else:
    70	            return set()
    71
    72	        for i in range(0, len(list_edges)):
    73	            Edge.add(list_edges[i])
    74
    75	        return Edge
    76
    77	    def adjacent(self, src, dst):
    78	        try:
    79	            t = self[src][dst]
    80	            a = True
    81	        except KeyError:
    82	            a = False
    83
    84	        return a
    85
    86	    def neighbors(self, vertex):
    87	        if vertex in self:
    88	            # return list(self[vertex].keys())
    89	            return set(self[vertex].keys())
    90	        else:
    91	            return set()
    92
    93	    def degree(self, vertex):
    94	        if vertex not in self:
    95	            keys = 0
    96	        else:
    97	            keys = len(list(self[vertex].keys()))
    98
    99	        return keys
   100
   101	    def path_valid(self, vertices):
   102	        paths = list(vertices)
   103	        valid = True
   104	        for i in range(len(paths) - 1):
   105	            if self.adjacent(paths[i], paths[i + 1]) is False:
   106	                valid = False
   107	                break
   108
   109	        return valid
   110
   111	    def path_length(self, vertices):
   112	        paths = list(vertices)
   113	        if self.path_valid(vertices) == False:
   114	            path_length = None
   115	        elif len(paths) > 1:
   116	            path_length = self[paths[0]][paths[1]]
   117	            for z in range(1, len(paths) - 1):
   118	                path_length += self[paths[z]][paths[z + 1]]
   119	        elif len(paths)<=1:
   120	            path_length = None
   121
   122	        return path_length
   123
   124	    # def is_connected(self):
   125	    #     t = True
   126	    #     keys = []
   127	    #     for a in self:
   128	    #         if self[a] == {}:
   129	    #             t = False
   130	    #             break
   131	    #         else:
   132	    #             for i in a:
   133	    #                 keys.append(i)
   134	    #             # keys.append(list(self[a].keys()))
   135	    #
   136	    #     if t is True:
   137	    #         for x in self:
   138	    #             if x not in keys:
   139	    #                 t = False
   140	    #                 break
   141	    #     return t
   142	    def is_connected(self):
   143	        vertex = list(self)
   144
   145	        for i in vertex:
   146	            vertex_copy = vertex.copy()
   147	            vertex_copy.remove(i)
   148	            for j in vertex:
   149	                if self.find_path(i, j) is None:
   150	                    return False
   151	        return True
   152
   153	    def find_path(self, start_vertex, end_vertex, path=None):
   154
   155	        """
   156	        find a path from start_vertex to end_vertex
   157	        in graph
   158	         https://www.python-course.eu/graphs_python.php
   159	        """
   160	        if path is None:
   161	            path = []
   162	        graph = self.copy()
   163	        path = path + [start_vertex]
   164	        if start_vertex == end_vertex:
   165	            return path
   166	        if start_vertex not in graph:
   167	            return None
   168	        for vertex in graph[start_vertex]:
   169	            if vertex not in path:
   170	                extended_path = self.find_path(vertex, end_vertex, path)
   171	                if extended_path:
   172	                    return extended_path
   173
   174	        return None

