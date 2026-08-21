"""
Decentralized consensus simulation for the STRUDEL research showcase.

This independently written public demo illustrates a core idea behind
decentralized learning: communication topology changes how quickly information
can propagate through a network.

It is not STRUDEL training code and does not reproduce private experiments.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from topology_utils import build_demo_topologies, fiedler_value


def metropolis_weight_matrix(graph: nx.Graph) -> np.ndarray:
    """
    Construct a symmetric Metropolis-Hastings consensus matrix.

    For each edge (i, j):
        w_ij = 1 / (1 + max(deg(i), deg(j)))

    The diagonal is chosen so every row sums to 1. For an undirected graph,
    this matrix is doubly stochastic, so average consensus is preserved.
    """
    nodes = list(graph.nodes())
    index = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)

    weights = np.zeros((n, n), dtype=float)
    degrees = dict(graph.degree())

    for u, v in graph.edges():
        weight = 1.0 / (1.0 + max(degrees[u], degrees[v]))
        i, j = index[u], index[v]
        weights[i, j] = weight
        weights[j, i] = weight

    for i in range(n):
        weights[i, i] = 1.0 - weights[i].sum()

    return weights


def consensus_error(
    graph: nx.Graph,
    initial_values: np.ndarray,
    rounds: int = 60,
) -> np.ndarray:
    """Return root-mean-square disagreement from the global mean over time."""
    weights = metropolis_weight_matrix(graph)
    state = initial_values.astype(float).copy()
    target = float(initial_values.mean())

    errors = [np.sqrt(np.mean((state - target) ** 2))]

    for _ in range(rounds):
        state = weights @ state
        errors.append(np.sqrt(np.mean((state - target) ** 2)))

    return np.asarray(errors)


def main() -> None:
    rng = np.random.default_rng(7)
    topologies = build_demo_topologies()
    initial_values = rng.normal(size=25)

    output_dir = Path(".")
    csv_path = output_dir / "consensus_results.csv"
    figure_path = output_dir / "consensus_convergence.png"

    rows = []
    plt.figure(figsize=(8, 5))

    for name, graph in topologies.items():
        errors = consensus_error(graph, initial_values)

        plt.plot(
            range(len(errors)),
            errors,
            label=f"{name} (Fiedler={fiedler_value(graph):.3f})",
        )

        for round_number, error in enumerate(errors):
            rows.append(
                {
                    "topology": name,
                    "round": round_number,
                    "rmse_disagreement": error,
                }
            )

    plt.yscale("log")
    plt.xlabel("Consensus round")
    plt.ylabel("RMSE disagreement from global mean")
    plt.title("Effect of Communication Topology on Consensus Speed")
    plt.legend()
    plt.tight_layout()
    plt.savefig(figure_path, dpi=180)
    plt.close()

    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["topology", "round", "rmse_disagreement"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {csv_path}")
    print(f"Wrote {figure_path}")


if __name__ == "__main__":
    main()
