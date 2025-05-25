def build_rna_graph(sequence_length, basepairs):
    graph = {i: [] for i in range(sequence_length)}
    
    # Add backbone edges (linear chain)
    for i in range(sequence_length - 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)
    
    # Add basepair edges
    for i, j in basepairs:
        graph[i].append(j)
        graph[j].append(i)
    
    return graph
