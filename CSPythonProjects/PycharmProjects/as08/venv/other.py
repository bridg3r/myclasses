
"""
  2	Dictionary representation of Graph
  3	"""
class Edges(dict):
    "Edges class"
def __init__(self, graph=None):

super(Edges, self).__init__()

self.graph = graph
def __setitem__(self, key, value):
    14
    if self.graph is not None:
        15
    if key not in self.graph:
        16
    self.graph.__missing__(key)
super(Edges, self).__setitem__(key, value)
def copy(self, graph=None):
    21
    edge_graph = Edges()


22
edge_graph.graph = graph
23
if self != {}:
    24
    for w in self:
        25
    edge_graph[w] = self[w]
26
return edge_graph
27
28
29


class Graph(dict):
    30
    " Graph class"


31
32


def __missing__(self, key):
    33
    self[key] = Edges(graph=self)


34
return self[key]
35
36


def __delitem__(self, key):
    37
    self.pop(key)


38
for a in self:
    39
    if self[a] != {}:
        40
    if key in self[a]:
        41
    self[a].pop(key)
42
43


def __len__(self):
    44
    return len(self.keys())


45
46


def copy(self):
    47
    copy_graph = Graph()


48
for i in self:
    49
    copy_graph[i] = self[i].copy(graph=copy_graph)
50
51
return copy_graph
52
53


def vertices(self):
    54
    return set(self.keys())


55
56


def edges(self):
    57
    list_edges = []


58
for q in self:
    59
    if self[q] != {}:
        60
    for i in self[q].keys():
        61
    a = (q, i, self[q][i])
62
list_edges.append(a)
63
64
if len(list_edges) != 0:
    65
    Edge = {list_edges[0]}
66 else:
67
return set()
68
for i in range(0, len(list_edges)):
    69
    Edge.add(list_edges[i])
70
return Edge
71
72


def adjacent(self, src, dst):
    73
    if dst in self[src]:
        74
    return True


75
return False
76
77


def neighbors(self, vertex):
    78
    if vertex in self:
        79  # return list(self[vertex].keys())


80
return set(self[vertex].keys())
81 else:
82
return set()
83
84


def degree(self, vertex):
    85
    if vertex not in self:
        86
    keys = 0


87 else:
88
keys = len(list(self[vertex].keys()))
89
90
return keys
91
92


def path_valid(self, vertices):
    93
    paths = list(vertices)


94
valid = True
95
for i in range(len(paths) - 1):
    96
    if self.adjacent(paths[i], paths[i + 1]) is False:
        97
    valid = False
98
break
99
100
return valid
101
102


def path_length(self, vertices):
    103
    paths = list(vertices)


104
if self.path_valid(vertices) is False:
    105
    path_length = None
106 elif len(paths) > 1:
107
path_length = self[paths[0]][paths[1]]
108
for z in range(1, len(paths) - 1):
    109
    path_length += self[paths[z]][paths[z + 1]]
110 elif len(paths) <= 1:
111
path_length = None
112
113
return path_length
114
115


def is_connected(self):
    116
    vertex = list(self)


117
118
for i in vertex:
    119
    vertex_copy = vertex.copy()
120
vertex_copy.remove(i)
121
for j in vertex:
    122
    if self.find_path(i, j) is None:
        123
    return False
124
return True
125
126


def find_path(self, start_vertex, end_vertex, path=None):
    127


128
"""
129	        find a path from start_vertex to end_vertex
130	        in graph
131	         https://www.python-course.eu/graphs_python.php
132	        """
133
if path is None:
    134
    path = []
135
graph = self.copy()
136
path = path + [start_vertex]
137
if start_vertex == end_vertex:
    138
    return path
139
if start_vertex not in graph:
    140
    return None
141
for vertex in graph[start_vertex]:
    142
    if vertex not in path:
        143
    extended_path = self.find_path(vertex, end_vertex, path)
144
if extended_path:
    145
    return extended_path
146
147
return None