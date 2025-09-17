import pytest
from app.dijkstra import shortest_path, DijkstraError


def test_direct_connection():
    graph = {"A": {"B": 5}, "B": {}}
    dist, path = shortest_path(graph, "A", "B")
    assert dist == 5
    assert path == ["A", "B"]


def test_indirect_connection():
    graph = {"A": {"B": 2}, "B": {"C": 3}, "C": {}}
    dist, path = shortest_path(graph, "A", "C")
    assert dist == 5
    assert path == ["A", "B", "C"]


def test_unreachable():
    graph = {"A": {"B": 1}, "B": {}, "C": {}}
    dist, path = shortest_path(graph, "A", "C")
    assert dist is None
    assert path == []


def test_invalid_source():
    graph = {"A": {"B": 1}, "B": {}}
    with pytest.raises(DijkstraError):
        shortest_path(graph, "X", "B")
