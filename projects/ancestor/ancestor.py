class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exist add a connection from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(anc, s_node):
    graph = Graph()
    for i in anc:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[1], i[0])
    mp_len = 1
    earliest_ancestor = -1
    queue = Queue()
    queue.enqueue([s_node])
    while queue.size() > 0:
        path = queue.dequeue()
        vertex = path[-1]
        if (len(path) >= mp_len and vertex < earliest_ancestor) or (len(path) > mp_len):
            earliest_ancestor = vertex
            mp_len = len(path)
        for x in graph.vertices[vertex]:
            p_copy = list(path)
            p_copy.append(x)
            queue.enqueue(p_copy)

    return earliest_ancestor