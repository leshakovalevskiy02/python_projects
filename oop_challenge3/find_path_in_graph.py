from collections import deque
from math import inf

class Vertex:
    def __init__(self):
        self._links = []
        
    @property
    def links(self):
        return self._links
    
    
class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1
        
    @property
    def v1(self):
        return self._v1
    
    @property
    def v2(self):
        return self._v2
    
    @property
    def dist(self):
        return self._dist
    
    @dist.setter
    def dist(self, new_dist):
        self._dist = new_dist
        
    def __eq__(self, other):
        return {self.v1, self.v2} == {other.v1, other.v2}
    

class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []
        
    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)
    
    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
            for v in (link.v1, link.v2):
                if v not in self._vertex:
                    self._vertex.append(v)
                v._links.append(link)
        
    def find_path(self, start_v, stop_v):
        min_values = [0] + [inf] * (len(self._vertex) - 1)
        min_vertex_values = dict(zip(self._vertex, min_values))
        queue = deque([self._vertex[0]])
        
        while queue:
            vertex = queue.popleft()
            links = vertex.links
            for link in links:
                if link.v1 == vertex:
                    if min_vertex_values[vertex] + link.dist < min_vertex_values[link.v2]:
                        min_vertex_values[link.v2] = min_vertex_values[vertex] + link.dist
                        queue.append(link.v2)
                elif link.v2 == vertex:
                    if min_vertex_values[vertex] + link.dist < min_vertex_values[link.v1]:
                        min_vertex_values[link.v1] = min_vertex_values[vertex] + link.dist
                        queue.append(link.v1)
        
        links_between_start_stop_v = []
        vertexes_between_start_stop_v = [stop_v]
        vertex = stop_v
        while vertex != start_v:
            for link in vertex.links:
                if link.v1 == vertex and min_vertex_values[vertex] - link.dist == min_vertex_values[link.v2]:
                    vertexes_between_start_stop_v.append(link.v2)
                    vertex = link.v2
                    links_between_start_stop_v.append(link)
                elif link.v2 == vertex and min_vertex_values[vertex] - link.dist == min_vertex_values[link.v1]:
                    vertexes_between_start_stop_v.append(link.v1)
                    vertex = link.v1
                    links_between_start_stop_v.append(link)
        return vertexes_between_start_stop_v[::-1], links_between_start_stop_v[::-1]


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name

class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self.dist = dist


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7