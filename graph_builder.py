import networkx as nx
import matplotlib.pyplot as plt

def build_rna_graph(sequence_length, basepairs):
    G = nx.Graph()
    
    # Add nucleotides
    G.add_nodes_from(range(1, sequence_length + 1))
    
    # Add basepair edges
    for i, j in basepairs:
        G.add_edge(i, j, type='basepair')
    
    return G

def book_embedding(rna_sequence, pages):
    n = len(rna_sequence)
    
    for page in pages:
        graph = build_rna_graph(n, page)  # Pass each page's edges
        
        pos = {i: (i, 0) for i in range(1, n + 1)}
        plt.figure(figsize=(12, 6))
        
        print(graph.edges)
        nx.draw_networkx_edges(graph, pos, edge_color="blue", width=2, arrowstyle='-', arrows=True, connectionstyle=f'arc3, rad = {-0.4}')
        
        # Draw nodes and labels
        nx.draw_networkx_nodes(graph, pos, node_color="black", node_size=50)
        nx.draw_networkx_labels(graph, pos, font_size=8, font_color="white", font_weight="bold")
        plt.title("Book Embedding of RNA Structure")
        plt.axis("off")
        plt.show()

# Example usage
rna_sequence = "ACGUACGUA"
basepairs = [(1, 9), (2, 8), (3, 7)]  # Example basepairs
book_embedding(rna_sequence, [basepairs])

