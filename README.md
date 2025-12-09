# Optimal Placement of Wireless Transmitters
## Analysis of the Maximum Independent Set Problem

This repository contains the source code and final report for the Analysis of Algorithms project on **Wireless Transmitter Placement**. We model the problem of placing non-interfering wireless transmitters as finding the **Maximum Independent Set (MIS)** in an intersection graph.

### Project Contents

*   **`report.pdf`**: The complete project report in IEEE conference format. Contains the formal NP-Completeness proof, theoretical bounds, algorithmic details, and experimental analysis.
*   **`independent_set_solver.py`**: Python implementation of two algorithms for the MIS problem:
    1.  **Exact Algorithm**: A recursive backtracking approach (optimal but exponential time).
    2.  **Greedy Heuristic**: A minimum-degree polynomial-time approximation.
*   **`visualize_*.py`**: Helper scripts used to generate the figures in the report:
    *   `visualize_reduction.py`: Visualizes the 3-SAT to Independent Set reduction gadget.
    *   `visualize_greedy_fail.py`: Generates the counter-example graph where the greedy strategy fails.
    *   `visualize_phase_transition.py`: Generates the heatmap showing the phase transition of solution size vs. graph density.
*   **`report.tex`**: The LaTeX source code for the report.

### Running the Code

Prerequisites: `networkx`, `matplotlib`, `numpy`.

```bash
pip install networkx matplotlib numpy
```

To run the main solver and reproduce the experimental results (Time vs N, Greedy Ratio, etc.):

```python
python independent_set_solver.py
```

To generate specific visualizations:

```bash
python visualize_reduction.py
python visualize_phase_transition.py
```

### Key Results

*   **Complexity**: Proved NP-Complete via reduction from 3-SAT.
*   **Phase Transition**: Observed a sharp drop in independent set size as graph connectivity increases, consistent with probabilistic bounds.
*   **Greedy Performance**: The greedy degree-based heuristic provides near-optimal solutions (>90% approximation ratio) in negligible time for random graphs, making it suitable for practical network design.

