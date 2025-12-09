import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def exact_independent_set_size(G):
    """
    Helper to get exact MIS size.
    MIS(G) = MaxClique(Complement(G))
    """
    G_comp = nx.complement(G)
    if G_comp.number_of_nodes() == 0:
        return 0
    # nx.find_cliques returns a generator of all maximal cliques
    return max(len(c) for c in nx.find_cliques(G_comp))

def visualize_phase_transition():
    print("Generating Phase Transition Heatmap...")
    
    # Parameters
    ns = range(5, 31, 5) # N from 5 to 30
    ps = np.linspace(0.1, 0.9, 9) # p from 0.1 to 0.9
    
    # Data matrix
    data = np.zeros((len(ns), len(ps)))
    
    # Run simulation
    for i, n in enumerate(ns):
        for j, p in enumerate(ps):
            # Average over 5 trials for smoothness
            total_size = 0
            trials = 5
            for _ in range(trials):
                G = nx.erdos_renyi_graph(n, p)
                total_size += exact_independent_set_size(G)
            avg_size = total_size / trials
            data[i, j] = avg_size
            print(f"N={n}, p={p:.1f} -> Avg MIS Size: {avg_size:.2f}")

    # Plotting
    plt.figure(figsize=(10, 8))
    plt.imshow(data, cmap='viridis', interpolation='nearest', origin='lower')
    plt.colorbar(label='Avg Independent Set Size')
    
    # Ticks
    plt.xticks(np.arange(len(ps)), [f"{p:.1f}" for p in ps])
    plt.yticks(np.arange(len(ns)), ns)
    
    plt.xlabel("Graph Density (p)")
    plt.ylabel("Number of Nodes (N)")
    plt.title("Phase Transition of Maximum Independent Set Size\n(Heatmap of Avg MIS Size)")
    
    # Annotate values
    for i in range(len(ns)):
        for j in range(len(ps)):
            plt.text(j, i, f"{data[i, j]:.1f}", ha="center", va="center", color="white" if data[i, j] < data.max()/2 else "black")

    plt.savefig('phase_transition.png')
    print("Generated phase_transition.png")

if __name__ == "__main__":
    visualize_phase_transition()
