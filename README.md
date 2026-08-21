# Decentralized Deep Learning & Communication Topologies

**Research showcase from the UC Santa Cruz Science Internship Program (SIP)**

This repository summarizes my work on **decentralized deep learning and structured communication topologies** through the UCSC Science Internship Program. I worked on a three-person research team under PhD mentorship, using Python and PyTorch to study how communication structure affects distributed learning systems.

> **Source-code note:** The underlying STRUDEL research platform is maintained in a private collaborative research repository. This public repository documents my research experience and independently created portfolio material; private source code and restricted research files are not reproduced here.

## Research Question

In decentralized learning, participating agents exchange information directly with other agents rather than relying entirely on a central server.

Our work investigated a key systems question:

**How does the communication topology connecting those agents influence connectivity, information flow, and decentralized learning performance?**

Instead of treating network structure as an implementation detail, we studied it as an experimental variable.

## My Role

As a student research intern, I:

* Conducted decentralized-learning experiments using **Python and PyTorch**
* Worked with structured communication graphs connecting multiple learning agents
* Compared network topologies and their connectivity properties
* Analyzed experimental results and model behavior
* Helped document methods, findings, and architecture comparisons for a research manuscript
* Collaborated with a PhD mentor and a three-person student research team

## Communication Topologies

Our experiments considered network structures including:

* **Fully Connected**
* **Torus**
* **Tree**
* **Butterfly**
* **Stochastic Block Model (SBM)**

Each topology creates a different balance between communication cost and the ability of information to move efficiently throughout the network.

## Graph Connectivity

One metric we examined was the **Fiedler value**, the second-smallest eigenvalue of a graph's Laplacian matrix.

It provides a quantitative way to reason about network connectivity: larger values generally indicate stronger connectivity and potentially faster information propagation through the communication graph.

In one 25-client topology comparison, we observed approximately:

| Topology  |                         Fiedler Value |
| --------- | ------------------------------------: |
| Torus     |                                 1.382 |
| Butterfly |                                 0.238 |
| Tree      |                                0.0535 |
| SBM       | ~0.51–0.98 depending on configuration |

These comparisons helped illustrate how dramatically communication structure can change the connectivity of a decentralized-learning system.

## Experimental Context

The research used the **STRUDEL** experimental platform for structured federated and decentralized learning.

Our work involved:

* Multi-agent learning systems
* Non-centralized communication
* Structured network topologies
* Neural-network training
* Image-classification experiments
* Distributed data partitions
* Quantitative comparison of communication structures

## What I Learned

This project changed how I think about machine learning systems.

Model architecture is only one component of a distributed ML system. Performance can also depend on:

* how data is distributed,
* which agents communicate,
* how information propagates through the network,
* the optimization procedure,
* and the communication cost required to coordinate learning.

The project gave me experience moving from simply **building models** to asking and experimentally investigating **research questions about machine-learning systems**.

## Technologies & Concepts

`Python` · `PyTorch` · `Decentralized Learning` · `Federated Learning` · `Deep Learning` · `Graph Theory` · `Network Topology` · `Experimental Design` · `Model Evaluation`

## About This Repository

This is a **research portfolio repository**, not a copy of the private STRUDEL codebase.

Additional pages in this repository document the research methodology, topology analysis, and my individual experience working on the project.
