# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
import networkx as nx
import pytest

from libs.collatz.collatz import CollatzSequences


def test_collatz_sequences_init():
    with pytest.raises(ValueError):
        CollatzSequences(0, 10)

    with pytest.raises(ValueError):
        CollatzSequences(10, 10)

    collatz = CollatzSequences(1, 10)
    assert isinstance(collatz.sequences, dict)
    assert collatz.graph is not None


def test_compute_sequences():
    collatz = CollatzSequences(1, 10)
    assert collatz.sequences[1] == [1]
    assert collatz.sequences[2] == [2, 1]
    assert collatz.sequences[3] == [3, 10, 5, 16, 8, 4, 2, 1]
    assert collatz.sequences[4] == [4, 2, 1]
    assert collatz.sequences[5] == [5, 16, 8, 4, 2, 1]
    assert collatz.sequences[6] == [6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert collatz.sequences[7] == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz.sequences[8] == [8, 4, 2, 1]
    assert collatz.sequences[9] == [
        9,
        28,
        14,
        7,
        22,
        11,
        34,
        17,
        52,
        26,
        13,
        40,
        20,
        10,
        5,
        16,
        8,
        4,
        2,
        1,
    ]


def test_as_graph():
    collatz = CollatzSequences(1, 10)
    graph = collatz.graph
    assert isinstance(graph, nx.DiGraph)
    assert graph.has_edge(1, 4)
    assert graph.has_edge(4, 2)
    assert graph.has_edge(2, 1)
    assert graph.has_edge(3, 10)
    assert graph.has_edge(5, 16)
    assert graph.has_edge(16, 8)
    assert graph.has_edge(8, 4)
    assert graph.has_edge(6, 3)
    assert graph.has_edge(7, 22)
    assert graph.has_edge(22, 11)
    assert graph.has_edge(11, 34)
    assert graph.has_edge(34, 17)
    assert graph.has_edge(17, 52)
    assert graph.has_edge(52, 26)
    assert graph.has_edge(26, 13)
    assert graph.has_edge(13, 40)
    assert graph.has_edge(40, 20)
    assert graph.has_edge(20, 10)
    assert graph.has_edge(9, 28)
    assert graph.has_edge(28, 14)
    assert graph.has_edge(14, 7)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
