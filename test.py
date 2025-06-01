from book_embedding import is_two_page_embeddable
import networkx as nx

def k_2_5_graph():
    vertices = ['u1', 'u2', 'v1', 'v2', 'v3', 'v4', 'v5']
    edges = [
        ('u1', 'v1'), ('u1', 'v2'), ('u1', 'v3'), ('u1', 'v4'), ('u1', 'v5'),
        ('u2', 'v1'), ('u2', 'v2'), ('u2', 'v3'), ('u2', 'v4'), ('u2', 'v5')
    ]
    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    graph.add_edges_from(edges)

    assert is_two_page_embeddable(graph) == True

def k_5_graph():
    vertices = ['A', 'B', 'C', 'D', 'E']

    edges = [
        ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'),
        ('B', 'C'), ('B', 'D'), ('B', 'E'),
        ('C', 'D'), ('C', 'E'),
        ('D', 'E')
    ]

    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    graph.add_edges_from(edges)

    assert is_two_page_embeddable(graph) == False
