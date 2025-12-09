import networkx as nx
import matplotlib.pyplot as plt

def visualize_greedy_fail():
    # Counter example:
    # A central node connected to 3 leaves.
    # And those 3 leaves connected to each other? No.
    # Standard counter example:
    # Path graph: 1-2-3-4.
    # Degrees: 1, 2, 2, 1.
    # Greedy picks min degree 1 (say node 1). Removes 1 and 2. Remaining: 3-4. Picks 3 (or 4). Total size 2.
    # Exact: {1, 3} or {1, 4} or {2, 4}? {1, 4} is size 2. {2, 3} is invalid.
    # Wait, path 1-2-3-4. IS: {1, 3} size 2. {1, 4} size 2. {2, 4} size 2.
    # Greedy picks 1. Removes 2. Left 3-4. Picks 3. Size 2.
    # That works.
    
    # Better counter example:
    # 6-cycle: 1-2-3-4-5-6-1. All degree 2.
    # Greedy picks any, say 1. Removes 2, 6. Left 3-4-5.
    # Picks 3 (degree 1 in remaining). Removes 4. Left 5. Picks 5.
    # Set: {1, 3, 5}. Size 3.
    # Exact: {1, 3, 5} or {2, 4, 6}. Size 3.
    
    # We need a case where min degree choice is bad.
    # Example:
    # Node u connected to v1, v2, ..., vk.
    # Each vi connected to a clique?
    
    # Let's use the classic "Crown Graph" or similar.
    # Or simply:
    # 0 connected to 1, 2, 3, 4, 5, 6
    # 1 connected to 2
    # 3 connected to 4
    # 5 connected to 6
    # Degrees:
    # 0: 6
    # 1: 2 (0, 2)
    # 2: 2 (0, 1)
    # ...
    # Min degree is 2.
    # Greedy picks 1. Removes 0, 2.
    # Remaining: 3-4, 5-6.
    # Picks 3. Removes 4.
    # Picks 5. Removes 6.
    # Result: {1, 3, 5}. Size 3.
    # Exact: Pick 0? No, that gives size 1.
    # Exact: {1, 3, 5} is size 3. {2, 4, 6} is size 3.
    
    # Let's try:
    # A central node 'c' connected to leaves 'l1', 'l2'.
    # 'l1' connected to 'k1', 'k2'.
    # 'l2' connected to 'k3', 'k4'.
    # Degrees: c:2, l1:3, l2:3, k1:1, k2:1, k3:1, k4:1.
    # Greedy picks k1 (deg 1). Removes l1.
    # Remaining: c connected to l2. l2 connected to k3, k4.
    # Degrees: c:1, l2:3, k3:1, k4:1.
    # Greedy picks c (deg 1). Removes l2.
    # Remaining: k3, k4.
    # Picks k3. Picks k4.
    # Result: {k1, c, k3, k4}. Size 4.
    # Exact: {k1, k2, k3, k4, c} is valid? No, c connected to l1, l2.
    # IS: {k1, k2, k3, k4, c} -> c not connected to k's.
    # Edges: (c, l1), (c, l2), (l1, k1), (l1, k2), (l2, k3), (l2, k4).
    # IS: {k1, k2, k3, k4, c}. Size 5.
    # Greedy found size 4.
    # THIS IS IT!
    
    G = nx.Graph()
    edges = [
        ('c', 'l1'), ('c', 'l2'),
        ('l1', 'k1'), ('l1', 'k2'),
        ('l2', 'k3'), ('l2', 'k4')
    ]
    G.add_edges_from(edges)
    
    pos = {
        'c': (0, 0),
        'l1': (-1, 1), 'l2': (1, 1),
        'k1': (-2, 2), 'k2': (0, 2),
        'k3': (0, 2), 'k4': (2, 2) # Overlap fix needed
    }
    pos['k2'] = (-0.5, 2)
    pos['k3'] = (0.5, 2)
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12)
    plt.title("Greedy Failure Case\nGreedy picks leaves first -> Size 4 ({k1, c, k3, k4})\nOptimal -> Size 5 ({k1, k2, c, k3, k4})")
    plt.savefig('greedy_failure.png')
    print("Generated greedy_failure.png")

if __name__ == "__main__":
    visualize_greedy_fail()
