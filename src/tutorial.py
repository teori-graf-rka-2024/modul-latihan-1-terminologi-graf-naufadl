import networkx as nx 
import matplotlib.pyplot as plt
import graph as gh

G = gh.create_graph([
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 1),  
    (1, 5),  
    (2, 6),  
    (3, 7),  
    (4, 8),  
    (5, 9)   
])

gh.get_degree(G, 9)
        
gh.dfs_traversal(G, 5)

gh.bfs_traversal(G, 3)

print(gh.find_shortest_path(G, 1, 7))

gh.visualize_graph(G)