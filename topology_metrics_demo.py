"""
Public demonstration of graph-connectivity analysis used in my
decentralized-learning research.

This file is independently written for this portfolio and does not
contain source code from the private STRUDEL research repository.
"""

import numpy as np
import networkx as nx


def fiedler_value(graph: nx.Graph) -> float:
    """
    Return the second-smallest eigenvalue of the combinatorial
    graph Laplacian, also known as the Fiedler value.
    """
    laplacian = nx.laplacian_matrix(graph).toarray().astype(float)
    eigenvalues = np.linalg.eigvalsh(laplacian)
    eigenvalues.sort()

    if len(eigenvalues) < 2:
        return 0.0

    return float(eigenvalues[1])


def binary_tree(n: int) -> nx.Graph:
    """Construct a simple binary tree with n nodes."""
    graph = nx.Graph()
    graph.add_nodes_from(range(n))

    for child in range(1, n):
        parent = (child - 1) // 2
        graph.add_edge(parent, child)

    return graph


def torus_grid(side_length: int) -> nx.Graph:
    """
    Construct a 2D periodic grid (torus).

    A 5 x 5 grid produces 25 participating nodes.
    """
    graph = nx.grid_2d_graph(
        side_length,
        side_length,
        periodic=True,
    )

    return nx.convert_node_labels_to_integers(graph)


def stochastic_block_network(n: int = 25) -> nx.Graph:
    """
    Construct an illustrative stochastic block model with three
    communities.

    Probabilities here are chosen only for demonstration and are
    not copied from private research configurations.
    """
    sizes = [8, 8, n - 16]

    probabilities = [
        [0.65, 0.10, 0.10],
        [0.10, 0.65, 0.10],
        [0.10, 0.10, 0.65],
    ]

    return nx.stochastic_block_model(
        sizes,
        probabilities,
        seed=42,
    )


def summarize(name: str, graph: nx.Graph) -> None:
    """Print basic connectivity statistics for a graph."""
    average_degree = (
        sum(dict(graph.degree()).values()) / graph.number_of_nodes()
    )

    print(f"{name}")
    print(f"  nodes:          {graph.number_of_nodes()}")
    print(f"  edges:          {graph.number_of_edges()}")
    print(f"  average degree: {average_degree:.2f}")
    print(f"  Fiedler value:  {fiedler_value(graph):.4f}")
    print()


def main() -> None:
    n = 25

    topologies = {
        "Fully connected": nx.complete_graph(n),
        "Torus (5 x 5)": torus_grid(5),
        "Binary tree": binary_tree(n),
        "Stochastic block model": stochastic_block_network(n),
    }

    print("Communication Topology Connectivity Demo")
    print("=" * 42)
    print()

    for name, graph in topologies.items():
        summarize(name, graph)


if __name__ == "__main__":
    main()
