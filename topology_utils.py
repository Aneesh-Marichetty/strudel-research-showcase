"""
Public graph utilities for the STRUDEL research showcase.

This module is independently written portfolio code. It does not reproduce
source code, configuration files, or unpublished materials from the private
STRUDEL research repository.
"""

from __future__ import annotations

import networkx as nx
import numpy as np


def fiedler_value(graph: nx.Graph) -> float:
    """Return the second-smallest eigenvalue of the combinatorial Laplacian."""
    if graph.number_of_nodes() < 2:
        return 0.0

    laplacian = nx.laplacian_matrix(graph).toarray().astype(float)
    eigenvalues = np.linalg.eigvalsh(laplacian)
    eigenvalues.sort()
    return float(eigenvalues[1])


def binary_tree(n: int) -> nx.Graph:
    """Construct a simple binary tree with n nodes."""
    if n < 1:
        raise ValueError("n must be at least 1")

    graph = nx.Graph()
    graph.add_nodes_from(range(n))

    for child in range(1, n):
        parent = (child - 1) // 2
        graph.add_edge(parent, child)

    return graph


def torus_grid(side_length: int) -> nx.Graph:
    """Construct a 2D periodic square grid and relabel nodes as integers."""
    if side_length < 2:
        raise ValueError("side_length must be at least 2")

    graph = nx.grid_2d_graph(
        side_length,
        side_length,
        periodic=True,
    )
    return nx.convert_node_labels_to_integers(graph)


def illustrative_sbm(seed: int = 42) -> nx.Graph:
    """
    Construct a connected illustrative stochastic block model with 25 nodes.

    The probabilities are chosen solely for this public demo and are not
    research configuration values from STRUDEL.
    """
    sizes = [8, 8, 9]
    probabilities = [
        [0.65, 0.10, 0.10],
        [0.10, 0.65, 0.10],
        [0.10, 0.10, 0.65],
    ]

    graph = nx.stochastic_block_model(
        sizes,
        probabilities,
        seed=seed,
    )

    # Make the public demo robust even if a sampled SBM is disconnected.
    components = [list(c) for c in nx.connected_components(graph)]
    for left, right in zip(components, components[1:]):
        graph.add_edge(left[0], right[0])

    return graph


def build_demo_topologies() -> dict[str, nx.Graph]:
    """Return the topology set used by the public portfolio demos."""
    n = 25
    return {
        "Fully connected": nx.complete_graph(n),
        "Torus (5 x 5)": torus_grid(5),
        "Binary tree": binary_tree(n),
        "Stochastic block model": illustrative_sbm(),
    }


def graph_metrics(graph: nx.Graph) -> dict[str, float]:
    """Calculate several interpretable graph-connectivity metrics."""
    n = graph.number_of_nodes()
    m = graph.number_of_edges()

    metrics = {
        "nodes": float(n),
        "edges": float(m),
        "average_degree": float(
            sum(dict(graph.degree()).values()) / n
        ),
        "density": float(nx.density(graph)),
        "fiedler_value": fiedler_value(graph),
    }

    if nx.is_connected(graph):
        metrics["diameter"] = float(nx.diameter(graph))
        metrics["average_shortest_path"] = float(
            nx.average_shortest_path_length(graph)
        )
    else:
        metrics["diameter"] = float("nan")
        metrics["average_shortest_path"] = float("nan")

    return metrics
