def is_two_page_embeddable(graph):
    vertices = list(graph.nodes())
    edges = list(graph.edges())

    # sort vertex order as we attempt to put it in a circle
    vertex_order = {v: i for i, v in enumerate(vertices)} 

    # Build an adjacency list for edge crossing groups
    edge_crossing_map = {}
    for i, e1 in enumerate(edges):
        edge_crossing_map[e1] = []
        # check if any of the edge cross with another edge
        for j, e2 in enumerate(edges):
            if i != j and edge_crosses(e1, e2, vertex_order):
                edge_crossing_map[e1].append(e2)
        
    # crossing edges must be in a different page
    return two_colorable(edges, edge_crossing_map)

def edge_crosses(edge1, edge2, vertex_order):
    # get the four nodes
    # get the position of the nodes in the sorted circle (vertex order)
    node1, node2 = sorted((vertex_order[edge1[0]], vertex_order[edge1[1]]))
    node3, node4 = sorted((vertex_order[edge2[0]], vertex_order[edge2[1]]))
    # it crosses x if the following is true for the node ordering in the circle
    # node1  node3                             node3     node1 
    #       x                    or                    x
    # node4   node2                            node2      node4
    return (node1 < node3 < node2 < node4) or (node3 < node1 < node4 < node2)

# Try to partition edges into two non-crossing sets (pages)
# if same color means two edges in a subset cross
def two_colorable(edges, edge_crossing_map):
    edge_colors = {}
    for edge in edges:
        if edge not in edge_colors:
            # start coloring with 0
            if not color_edge(edge_colors, edge, 0, edge_crossing_map):
                return False
    return True

def color_edge(edge_colors, edge, color, edge_crossing_map):
    # if edge is colored, we attempt to color with the same color, then its ok, if not, we have as crossing, thus returning false
    if edge in edge_colors:
        return edge_colors[edge] == color
    edge_colors[edge] = color
    for neighbor in edge_crossing_map[edge]:
        # 1 - color alternate the edge colors. Its crossing edge should be in a different subset
        if not color_edge(edge_colors, neighbor, 1 - color, edge_crossing_map): 
            return False
    return True
