# Kaupungit A–N sijaitsevat taulukon 1 koordinaattien esittämissä paikoissa (tavanomaisessa euklidisessa kaksiulotteisessa koordinaatistossa). Niistä pääsee kulkemaan yksisuuntaisia teitäpitkin toisiinsa taulukon 2 esittämällä tavalla. Muuten liikkuminen kaupunkien välillä onmahdotonta.

# a) Agenttisi tahtoo päästä mahdollisimman nopeasti kaupungista A kaupunkiin K ja käyttää Dijkstran algoritmia (uniform cost search) löytääkseen optimaalisen reitin. Mikä on tuo löytyvä reitti? Kuinka kauan matka tulee kestämään?

# b) Kuten a), mutta käytä A*-algoritmia käyttäen heuristiikkana suoraa linnuntie-etäisyyttä maaliin.

# c) Löytyykö tieverkoston suunnittelusta jotain huomautettavaa?
import math


class Node:

    def __init__(self, data, x, y, indexloc=None,):
        # Holds data of the node, like name of the node
        self.data = data
        # Index corresponds to its column in any given row in the adjacency matrix
        self.x = x
        self.y = y
        self.index = indexloc


class Graph:

    @classmethod
    def create_from_nodes(self, nodes):
        # Graph.create_from_nodes([a, b, c, d, e, f])
        return Graph(len(nodes), len(nodes), nodes)

    # Graph(6, 6, [a, b, c, d, e, f])
    def __init__(self, row, col, nodes=None):
        # Set up an adjacency matrix of only zeroes in row * col matrix
        self.adj_mat = [[0] * col for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            # Give every node its index
            self.nodes[i].index = i

    # Makes a connection between two nodes to the adjacency matrix with possible weight
    # Gets indexes from both nodes and adds weight to those indexes in the matrix
    def connect_two_nodes(self, node1, node2, weight=1):
        node1, node2 = self.get_index_from_node(
            node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = weight

    # Uses connect_two_nodes() to make the connections of two nodes to the adjacency matrix at the same time
    def connect(self, node1, node2, weight=1):
        self.connect_two_nodes(node1, node2, weight)

    # Row is always the same, column changes
    # for columns in a row (in adj_mat), if the value on the column in the row is not 0...
    # Return a list of tuples: the destination node and the weight of the connection
    def connections_from(self, node):
        node = self.get_index_from_node(node)
        return [(self.nodes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node])) if self.adj_mat[node][col_num] != 0]

    # Column is always the same, row changes
    # for rows in in the adjacency matrix, if the value of the column is not 0...
    # Return a list of tuples: the node of the current row and the weight of the connection
    def connections_to(self, node):
        node = self.get_index_from_node(node)
        column = [row[node] for row in self.adj_mat]
        return [(self.nodes[row_num], column[row_num]) for row_num in range(len(column)) if column[row_num] != 0]

    # Prints the adjacency matrix
    def print_adj_mat(self):
        for row in self.adj_mat:
            print(row)

    # Return a node of a certain index from 'nodes'
    def node(self, index):
        return self.nodes[index]

    # Gets indexes of two nodes
    # Sets the weighted connection value from a certain node to another node to 0
    def remove_connection(self, node1, node2):
        node1, node2 = self.get_index_from_node(
            node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = 0

    # Remove connections between two nodes in the adjacency matrix
    def remove_connections(self, node1, node2):
        self.remove_connection(node1, node2)

    # If the weighted value is not 0 between two nodes, return true
    def node_has_connection_to_node(self, node1, node2):
        node1, node2 = self.get_index_from_node(
            node1), self.get_index_from_node(node2)
        return self.adj_mat[node1][node2] != 0

    # If there is a connection from node1 to node2 or vice versa, return true
    def has_connection(self, node1, node2):
        return self.node_has_connection_to_node(node1, node2) or self.node_has_connection_to_node(node2, node1)

    # Adds a new node to 'nodes'
    # Sets an index for the new node
    # Adds the new node for every existing row in the adjacency matrix with no connections
    # Adds a new row to the adjacency matrix with no connections
    def add_node(self, node):
        self.nodes.append(node)
        node.index = len(self.nodes) - 1
        for row in self.adj_mat:
            row.append(0)
        self.adj_mat.append([0] * (len(self.adj_mat) + 1))

    # Gets the conncetion weight associated with travelling from node1 to node2
    def get_weight(self, node1, node2):
        node1, node2 = self.get_index_from_node(
            node1), self.get_index_from_node(node2)
        return self.adj_mat[node1][node2]

    # Get the index of the node
    def get_index_from_node(self, node):
        return node.index

    # Get the shortest path from source to target
    # Stores different path options and chooses the shortest one
    def dijkstra(self, source, target):
        # Initialize queue and sets
        queue = [source]
        visited = {}
        distance = {}
        shortest_distance = {}
        parent = {}

        # Populate initialized sets
        for node in range(len(self.adj_mat)):
            distance[node] = None
            visited[node] = False
            parent[node] = None
            shortest_distance[node] = float("inf")

        # Make source node's distance value 0
        distance[source.index] = 0

        # When queue is not empty...
        while queue:
            print("-----")
            print(distance)
            print(shortest_distance)
            print("queue:")
            for q in queue:
                print(q.data)
            # Pop first item from queue and make it the current node
            current = queue.pop(0)
            print("current: " + current.data)
            # Mark current node as visited
            visited[current.index] = True
            # If current node is the target...
            if current == target:
                # Show solution
                print(self.backtrace(parent, source, target))
                # End algorithm
                break
            # Get curret node's neighbor nodes
            neighbors = self.connections_from(current)
            # Iterate over neighbors:
            for neighbor in neighbors:
                # Store current iteration node from neighbor tuple to variable
                n = neighbor[0]
                print("neighbor: " + n.data)
                # If node hasn't been visited yet...
                if visited[n.index] == False:
                    # Add together current node's distance value and distance from this node to the neighbor
                    # Store the sum as the neighbor's distance value
                    distance[n.index] = distance[current.index] + \
                        self.get_weight(current, n)
                    print("distance: " + str(distance[n.index]))
                    print("shortest distance: " +
                          str(shortest_distance[n.index]))
                    # If neighbor's distance value is lower than its shortest distance value (INF by default)...
                    if distance[n.index] < shortest_distance[n.index]:
                        # Make neighbor's distance value as its shortest distance value
                        shortest_distance[n.index] = distance[n.index]
                        print("shortest distance: " +
                              str(shortest_distance[n.index]))
                        # Make current node a parent node for neighbour node
                        parent[n.index] = current
                        # Append neighbor node to queue
                        queue.append(n)
                    else:
                        print("drop " + n.data)
                else:
                    print("Already visited " + n.data)

    def a_star(self, source, target, h):
        # The set of discovered nodes that may need to be (re-)expanded.
        # Initially, only the start node is known.
        # This is usually implemented as a min-heap or priority queue rather than a hash-set.
        queue = [source]
        # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently known.
        cameFrom = [None for n in range(len(self.nodes))]
        # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
        gScore = [float("inf") for n in range(len(self.nodes))]
        gScore[source.index] = 0

        # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
        # how short a path from start to finish can be if it goes through n.
        fScore = [float("inf") for n in range(len(self.nodes))]
        fScore[source.index] = self.calculate_euclidean_distance(source)

        while queue:
            print("--- start of loop ---")
            # This operation can occur in O(1) time if openSet is a min-heap or a priority queue'
            # current := the node in openSet having the lowest fScore[] value
            lowest = queue[0]
            for n in queue:
                fs = fScore[n.index]
                if fs < fScore[lowest.index]:
                    lowest = n
            current = lowest

            for q in queue:
                print(q.data)
            print("current: " + current.data)

            if current == target:
                return self.reconstruct_path(cameFrom, current)

            queue.remove(current)
            print("--- neighbors ---")
            for neighbor in self.connections_from(current):
                n = neighbor[0]
                tentative_gScore = gScore[current.index] + self.get_weight(current, n)
                print("neighbor: " + n.data)
                print("tentative: " + str(tentative_gScore))
                print("g: " + str(gScore[n.index]))
                if tentative_gScore < gScore[n.index]:
                    cameFrom[n.index] = current
                    gScore[n.index] = tentative_gScore
                    fScore[n.index] = gScore[n.index] + self.calculate_euclidean_distance(n)
                    print("f: " + str(fScore[n.index]))
                    print(n.data + " came from " + cameFrom[n.index].data)
                    if n not in queue:
                        queue.append(n)
                    print("--- next ---")

        # Open set is empty but goal was never reached
        print("ERROR")

    def reconstruct_path(self, cameFrom, current):
        total_path = [current]
        
        while cameFrom[current.index] is not None:
            current = cameFrom[current.index]
            total_path.insert(0, current)
        return total_path

    def calculate_euclidean_distance(self, current):
        return math.sqrt((pow(current.x - 11, 2) + (pow(current.y - 9, 2))))

    def backtrace(self, parent, start, end):
        path = [end]
        print()
        while path[-1] != start:
            path.append(parent[path[-1].index])

        for i in range(len(path)):
            path[i] = path[i].data

        path.reverse()
        return path


def main():
    a = Node("A", 3, 1)
    b = Node("B", 5, 6)
    c = Node("C", 6, 4)
    d = Node("D", 1, 6)
    e = Node("E", 6, 1)
    f = Node("F", 3, 4)
    g = Node("G", 9, 3)
    h = Node("H", 10, 7)
    i = Node("I", 8, 10)
    j = Node("J", 4, 9)
    k = Node("K", 11, 9)
    l = Node("L", 11, 4)
    m = Node("M", 8, 6)
    n = Node("N", 1, 3)

    graph = Graph.create_from_nodes([a, b, c, d, e, f, g, h, i, j, k, l, m, n])

    graph.connect(a, e, 3)
    graph.connect(b, f, 3)
    graph.connect(b, m, 2)
    graph.connect(c, b, 5)
    graph.connect(c, f, 3)
    graph.connect(c, g, 4)
    graph.connect(d, j, 7)
    graph.connect(d, n, 3)
    graph.connect(e, c, 3)
    graph.connect(f, a, 3)
    graph.connect(f, d, 3)
    graph.connect(g, e, 4)
    graph.connect(g, h, 8)
    graph.connect(g, l, 6)
    graph.connect(g, m, 4)
    graph.connect(h, k, 3)
    graph.connect(h, m, 3)
    graph.connect(i, k, 4)
    graph.connect(j, b, 4)
    graph.connect(j, i, 5)
    graph.connect(l, k, 5)
    graph.connect(m, i, 4)
    graph.connect(n, a, 3)

    graph.print_adj_mat()

    # print("DIJKSTRA")
    # graph.dijkstra(a, k)
    print()
    print("A*")

    solution = graph.a_star(a, k, graph.a_star)
    solutionStr = ""

    for n in solution:
        solutionStr += n.data + " "

    print(solutionStr)

main()
