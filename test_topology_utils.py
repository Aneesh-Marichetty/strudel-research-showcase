"""Basic checks for the independently written public graph utilities."""

import math

import networkx as nx

from topology_utils import (
    binary_tree,
    fiedler_value,
    torus_grid,
)


def test_binary_tree_edges():
    graph = binary_tree(25)
    assert graph.number_of_nodes() == 25
    assert graph.number_of_edges() == 24
    assert nx.is_tree(graph)


def test_torus_size_and_degree():
    graph = torus_grid(5)
    assert graph.number_of_nodes() == 25
    assert all(degree == 4 for _, degree in graph.degree())


def test_known_fiedler_values():
    tree_value = fiedler_value(binary_tree(25))
    torus_value = fiedler_value(torus_grid(5))

    assert math.isclose(tree_value, 0.0535, rel_tol=0.03)
    assert math.isclose(torus_value, 1.3820, rel_tol=0.01)
