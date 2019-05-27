# 6.0002 Problem Set 5
# Graph optimization for shortest paths through MIT campus
import unittest
from graph import Digraph, Node, WeightedEdge

# Problem 2a: Designing your graph
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
# Answer: The nodes represent the building, while the edges represent the paths 
# from one building to another.


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph
    """
    
    graph = Digraph()
    parsed_nodes = {}       # dict of integer node index -> node object
    edges = []

    with open(map_filename) as f:
        data = f.readlines()
        for line in data:
            line = line.strip().split(' ')
            
            # Make the nodes
            if not line[0] in parsed_nodes:
                parsed_nodes[line[0]] = Node(line[0])
            if not line[1] in parsed_nodes:
                parsed_nodes[line[1]] = Node(line[1])
            
            # Make weighted edge
            dist = int(line[2])
            outdoor_dist = int(line[3])
            edge = WeightedEdge(parsed_nodes[line[0]], parsed_nodes[line[1]], dist, outdoor_dist)
            edges.append(edge)
    for node in parsed_nodes.values():
        graph.add_node(node)
    for edge in edges:
        graph.add_edge(edge)
    return graph

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out
# Answer: the test map is loaded in the __name__ == __main__ below.

# Problem 3a: Objective function
# What is the objective function for this problem? What are the constraints?
# Answer: The objective function is the distance_outdoors for a route. The constraint
# is to ensure the distance outdoors is lower than the max permitted.

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.
    """
    # print("called with start", start, 'path', path, 'best dist', best_dist, 'nbest path', best_path)
    # Need to find actual nodes from strings provided
    current_node = digraph.find_node_by_name(start)
    end_node = digraph.find_node_by_name(end)
    if current_node is None or end_node is None:
        raise ValueError('Invalid start or end node')
    
    # If we are done, return the current path, no need to explore children
    if str(start) == str(end):
        # print("start is end; returning", path, )
        return path
    
    # Loop thorugh all edges of this current node
    for edge in digraph.get_edges_for_node(current_node):
        child_name = edge.destination.name
        # print ('explroing children of', start, 'current edge is' , edge, ' with child name ', child_name )
        if child_name in path[0]:
            # To prevent cycles, ignore if path already contains this child
            # print('path is cyclical! Ignoring')
            continue
        elif path[2] + edge.get_outdoor_distance() > max_dist_outdoors:
            # ignore this child if it involves too much outdoors (doesnt meet constraint)
            # print('max dist', max_dist_outdoors, 'is too low for', path[2] + edge.get_outdoor_distance())
            continue
        
        # Call DFS on child, with new current path, containing that child and distances to it
        childs_path = [path[0] + [child_name], path[1] + edge.get_total_distance(), path[2] + edge.get_outdoor_distance()]
        # print('calling child path for child', child_name, childs_path)
        # This may return None if that branch of tree doesnt have target, or a path
        childs_best_path = get_best_path(digraph, child_name, end, childs_path, max_dist_outdoors, best_dist, best_path)
        if childs_best_path is not None:
            # print('found a real path!!!!', childs_best_path)
            # Update if it is acutally best and fits criteria
            if  childs_best_path[2] <= max_dist_outdoors and (best_dist is None or childs_best_path[1] < best_dist):
                # print("best dis", best_dist, "best path so far", best_path)
                best_path = childs_best_path
                best_dist = childs_best_path[1]
    # print('parent', start, 'is returning', best_path)
    return best_path

# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    best_dist = get_best_path(digraph, start, end, [[str(start)], 0, 0], max_dist_outdoors, None, None)
    if best_dist is None or best_dist[1] > max_total_dist:
        raise ValueError('No path possible with given constraints.')
    return best_dist[0]

# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")


    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    # def test_load_map():
    #     map = load_map('test_load_map.txt')
    #     return map
    # print (test_load_map())

    unittest.main()
    pass