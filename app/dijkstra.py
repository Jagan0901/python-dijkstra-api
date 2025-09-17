import heapq


class DijkstraError(Exception):
    """Custom exception for Dijkstra-related errors."""
    pass


def shortest_path(graph: dict, source: str, target: str):
    """
    Compute the shortest path in a weighted graph using Dijkstra's algorithm.

    Args:
        graph (dict): adjacency list with weights. Example:
            { "A": {"B": 5, "C": 2}, "B": {"C": 1}, "C": {"A": 4} }
        source (str): starting node
        target (str): ending node

    Returns:
        tuple: (distance, path) where
            distance (float or None): total weight of shortest path,
                                      or None if target not reachable
            path (list): list of nodes representing shortest path

    Raises:
        DijkstraError: if source or target not in graph.
    """
    if source not in graph:
        raise DijkstraError(f"Source node '{source}' not in graph")
    if target not in graph:
        raise DijkstraError(f"Target node '{target}' not in graph")

    # Distance dictionary
    distances = {node: float("inf") for node in graph}
    distances[source] = 0.0

    # Predecessor dictionary to rebuild path
    predecessors = {}

    # Priority queue
    queue = [(0.0, source)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_node == target:
            break

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            if weight < 0:
                raise DijkstraError("Graph contains negative weight edge")
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # If target not reached
    if distances[target] == float("inf"):
        return None, []

    # Reconstruct path
    path = []
    node = target
    while node in predecessors or node == source:
        path.append(node)
        if node == source:
            break
        node = predecessors[node]

    path.reverse()
    return distances[target], path
