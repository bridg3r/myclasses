"""
as09
"""

import collections
import sys
import math


def great_circle_distance(start, finish):
    """
    uses latitude/longitude coordinates to calculate the
    great_circle_distance between the two locations
    https://www.movable-type.co.uk/scripts/latlong.html
    """
    start_coordinate = city_coordinates[start]
    end_coordinate = city_coordinates[finish]
    lat1 = float(start_coordinate.split()[0])
    lat2 = float(end_coordinate.split()[0])
    lon1 = float(start_coordinate.split()[1])
    lon2 = float(end_coordinate.split()[1])
    r = 6371
    φ1 = lat1 * math.pi / 180
    φ2 = lat2 * math.pi / 180
    φ = (lat2 - lat1) * math.pi / 180
    λ = (lon2 - lon1) * math.pi / 180
    a = math.sin(φ / 2) * math.sin(φ / 2) + math.cos(φ1) * math.cos(φ2) * math.sin(λ / 2) * math.sin(λ / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c
    return d


def shortest_path(start, finish):
    start_cityid = city_names[start]
    finish_cityid = city_names[finish]
    shortest_distance = {}
    visited = {}
    unvisited = city_web.copy()
    path = []
    for node in unvisited:
        shortest_distance[node] = 9999999
    shortest_distance[start_cityid] = 0
    while unvisited:
        min_node = None
        for node in unvisited:
            if min_node is None or shortest_distance[node] < shortest_distance[min_node]:
                min_node = node
        for branch_node, weight in city_web[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[branch_node]:
                shortest_distance[branch_node] = weight + shortest_distance[min_node]
                visited[branch_node] = min_node
        unvisited.pop(min_node)
    current = finish_cityid
    while current != start_cityid:
        path.insert(0, current)
        current = visited[current]
    path.insert(0, start_cityid)
    return path


# create dictionary for coordinates of each city
lat_long = open('/Users/bridg3r/PycharmProjects/as09/city coordinates.txt')
lat_long = lat_long.readlines()
city_coordinates = {}
for x in lat_long:
    line = x.split()
    city_coordinates[int(line[0])] = line[1] + ' ' + line[2]
# create the graph
city_web = collections.defaultdict(dict)
edges = open('/Users/bridg3r/PycharmProjects/as09/edges')
edges = edges.readlines()
for x in edges:
    line = x.split()
    city_web[int(line[0])][int(line[1])] = great_circle_distance(int(line[0]), int(line[1]))
    city_web[int(line[1])][int(line[0])] = great_circle_distance(int(line[0]), int(line[1]))
# create dictionary for city names
cities = open('/Users/bridg3r/PycharmProjects/as09/venv/city names.txt')
cities = cities.readlines()
city_names = {}
city_ids = {}
for x in cities:
    line = x.split()
    number = line[0]
    city = ' '.join(line[1:])
    city_names[city] = int(number)
    city_ids[int(number)] = city
# outputs
argv = ('name', 'St. Vith', 'Salamanca', 'ophiolater')

if argv[1] not in city_names and argv[2] not in city_names:
    sys.exit("Error: Unknown cities: \'" + argv[1] + '\' and \'' + argv[2] + "\'")
elif argv[1] not in city_names:
    sys.exit("Error: Unknown city: \'" + argv[1] + "\'")
elif argv[2] not in city_names:
    sys.exit("Error: Unknown city: \'" + argv[2] +"\'")
elif shortest_path(argv[1], argv[2]) is None:
    sys.exit('No path from ' + argv[1] + ' to ' + argv[2] + '!')
if len(argv) == 3:
    for i in shortest_path(argv[1], argv[2]):
        print(city_ids[i])
if len(argv) == 4:
    print('https://www.google.com/maps/dir/', end='')
    for i in shortest_path(argv[1], argv[2]):
        j = city_coordinates[i].split()
        if i == shortest_path(argv[1], argv[2])[-1]:
            print("{:.3f}".format(float(j[0])) + ',' + "{:.3f}".format(float(j[1])))
        else:
            print("{:.3f}".format(float(j[0])) + ',' + "{:.3f}".format(float(j[1])) + '/', end='')


def shortest_path1(start, finish):
    """
    inputs two city names as strings and returns a list of ints that represent
    the city ID's of the path
    used some of the website below for reference
    https://www.geeksforgeeks.org/building-an-undirected-graph
    -and-finding-shortest-path-using-dictionaries-in-python/
    """
    start_cityid = city_names[start]
    finish_cityid = city_names[finish]
    explored = []
    queue = [[start_cityid]]
    if start_cityid == finish_cityid:
        return [start_cityid]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = city_web[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == finish_cityid:
                    return new_path
            explored.append(node)
    return None


def shortest_path3(start, finish):
    shortest_distance = {}
    graph = city_web.copy()
    visited = set()
    path = []
    for node in graph:   # initialize all nodes as infinity
        shortest_distance[node] = 9999999999
    shortest_distance[start] = 0
    current = start
    while current != finish:
        min_node = None
        for node in graph[current]:
            if node not in visited:
                if node not in shortest_distance or \
                        shortest_distance[node] > graph[current][node] + shortest_distance[current]:
                    shortest_distance[node] = graph[current][node] + shortest_distance[current]
                if min_node is None or shortest_distance[node] < shortest_distance[min_node]:
                    min_node = node
        visited.add(current)
        current = min_node  # go to node with lightest edge
    return 1, 2, 3


def shortest_path1(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    infinity = 9999999
    unseenNodes = graph
    path = []
    for node in unseenNodes:   # initialize all nodes as infinity
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    while unseenNodes:
        minimum_node = None
        for node in unseenNodes:
            if minimum_node is None:
                minimum_node = node
            elif shortest_distance[node] < shortest_distance[minimum_node]:
                minimum_node = node
        for childNode, weight in graph[minimum_node].items():
            if weight + shortest_distance[minimum_node] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minimum_node]
                predecessor[childNode] = minimum_node
        unseenNodes.pop(minimum_node)
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            sys.exit("No path from " + sys.argv[1] + " to " + sys.argv[2] + "!")
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        if len(sys.argv) == 3:
            for x1 in path:
                print(integer_id[x1])
        elif len(sys.argv) > 3:
            ending = ""
            for x2 in path:
                ending += "/" + coordinates0[x2][0] + "," + coordinates0[x2][1]
            print("https://www.google.com/maps/dir" + ending)