import networkx as nx
import matplotlib.pyplot as plt

def visualize_reduction():
    # Example Formula: (x1 v x2 v x3) ^ (~x1 v ~x2 v x4)
    # Clauses: C1 = {x1, x2, x3}, C2 = {~x1, ~x2, x4}
    
    G = nx.Graph()
    
    # Clause 1 Triangle
    G.add_edges_from([('x1_1', 'x2_1'), ('x2_1', 'x3_1'), ('x3_1', 'x1_1')])
    
    # Clause 2 Triangle
    G.add_edges_from([('~x1_2', '~x2_2'), ('~x2_2', 'x4_2'), ('x4_2', '~x1_2')])
    
    # Conflict Edges (x1 vs ~x1, x2 vs ~x2)
    G.add_edge('x1_1', '~x1_2')
    G.add_edge('x2_1', '~x2_2')
    
    pos = {
        'x1_1': (0, 1), 'x2_1': (1, 0), 'x3_1': (-1, 0),
        '~x1_2': (0, -1.5), '~x2_2': (1, -2.5), 'x4_2': (-1, -2.5)
    }
    
    # Adjust positions for better look
    pos['x1_1'] = (0, 2)
    pos['x2_1'] = (1, 1)
    pos['x3_1'] = (-1, 1)
    
    pos['~x1_2'] = (0, -1)
    pos['~x2_2'] = (1, -2)
    pos['x4_2'] = (-1, -2)

    plt.figure(figsize=(8, 6))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue')
    
    # Draw edges
    # Clause edges
    clause_edges = [('x1_1', 'x2_1'), ('x2_1', 'x3_1'), ('x3_1', 'x1_1'),
                    ('~x1_2', '~x2_2'), ('~x2_2', 'x4_2'), ('x4_2', '~x1_2')]
    nx.draw_networkx_edges(G, pos, edgelist=clause_edges, width=2, edge_color='black')
    
    # Conflict edges
    conflict_edges = [('x1_1', '~x1_2'), ('x2_1', '~x2_2')]
    nx.draw_networkx_edges(G, pos, edgelist=conflict_edges, width=2, edge_color='red', style='dashed')
    
    # Labels
    labels = {
        'x1_1': '$x_1$', 'x2_1': '$x_2$', 'x3_1': '$x_3$',
        '~x1_2': '$\\neg x_1$', '~x2_2': '$\\neg x_2$', 'x4_2': '$x_4$'
    }
    nx.draw_networkx_labels(G, pos, labels, font_size=16)
    
    plt.title("Reduction from 3-SAT to Independent Set\nFormula: $(x_1 \\vee x_2 \\vee x_3) \\wedge (\\neg x_1 \\vee \\neg x_2 \\vee x_4)$")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('reduction_example.png')
    print("Generated reduction_example.png")

if __name__ == "__main__":
    visualize_reduction()
