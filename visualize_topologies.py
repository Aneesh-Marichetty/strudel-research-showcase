"""
Visualize the public demo communication topologies.

All layouts and graph constructions here are independently created for this
portfolio. They are not exported from the private STRUDEL repository.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

from topology_utils import build_demo_topologies, graph_metrics


def layout_for(name: str, graph: nx.Graph):
    if name.startswith("Fully"):
        return nx.circular_layout(graph)
    if name.startswith("Torus"):
        return nx.spring_layout(graph, seed=4, iterations=150)
    if name.startswith("Binary"):
        return nx.spring_layout(graph, seed=9, iterations=150)
    return nx.spring_layout(graph, seed=12, iterations=150)


def main() -> None:
    topologies = build_demo_topologies()

    fig, axes = plt.subplots(2, 2, figsize=(10, 9))
    axes = axes.flatten()

    for axis, (name, graph) in zip(axes, topologies.items()):
        metrics = graph_metrics(graph)
        positions = layout_for(name, graph)

        nx.draw_networkx(
            graph,
            pos=positions,
            ax=axis,
            node_size=120,
            with_labels=False,
            width=0.8,
        )

        axis.set_title(
            f"{name}\n"
            f"edges={int(metrics['edges'])}, "
            f"Fiedler={metrics['fiedler_value']:.3f}"
        )
        axis.axis("off")

    plt.suptitle("Illustrative Communication Topologies")
    plt.tight_layout()
    plt.savefig("topology_gallery.png", dpi=180)
    plt.close()

    print("Wrote topology_gallery.png")


if __name__ == "__main__":
    main()
