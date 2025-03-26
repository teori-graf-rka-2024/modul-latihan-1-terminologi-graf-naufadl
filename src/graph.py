import networkx as nx 
import matplotlib.pyplot as plt

def create_graph (edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()

    if edges:
        G.add_edges_from(edges)
        
    print(G)
    return G
    
def get_degree(G: nx.Graph, node: int) -> int:
    if node not in G:
        print('Tidak ada node tersebut dalam graf')
        return None
    
    degrees = G.degree(node)
    print(degrees)
    return degrees
    
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    if start not in G:
        print('Node awal tidak ditemukan dalam graf')
        return []
    
    # Menggunakan fungsi bawaan NetworkX untuk DFS
    result = list(nx.dfs_preorder_nodes(G, source=start))
    print("Urutan DFS:", result)
    return result

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    if start not in G:
        print('Node awal tidak ditemukan dalam graf')
        return []
    
    # Menggunakan fungsi bawaan NetworkX untuk BFS
    result = list(nx.bfs_nodes(G, source=start))
    print("Urutan BFS:", result)
    return result

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    if source not in G or target not in G:
        print("Salah satu atau kedua simpul tidak ditemukan dalam graf")
        return []
    
    # Periksa apakah jalur ada
    if not nx.has_path(G, source, target):
        print(f"Tidak ada jalur dari {source} ke {target}")
        return []
    
    # Temukan jalur terpendek
    try:
        path = nx.shortest_path(G, source=source, target=target)
        print(f"Jalur terpendek dari {source} ke {target}: {path}")
        return path
    except nx.NetworkXNoPath:
        print(f"Tidak ada jalur dari {source} ke {target}")
        return []
        
def visualize_graph(G: nx.Graph) -> None:
    plt.figure(figsize=(10, 8))
    
    # Menentukan posisi node dengan layout yang lebih baik
    pos = nx.spring_layout(G, seed=42)  # Seed untuk konsistensi layout
    
    # Menggambar graf dengan styling yang lebih baik
    nx.draw(G, pos, 
            with_labels=True, 
            node_color='lightblue', 
            edge_color='gray', 
            node_size=1500, 
            font_size=10, 
            font_weight="bold",
            arrows=False)  # Tambahkan label node
    
    plt.title("Visualisasi Graf")
    
    # Simpan gambar
    plt.savefig("graph_visualization.png", format="png", dpi=300, bbox_inches='tight')
    
    # Tampilkan graf
    plt.show()
    
    # Tutup plot untuk mencegah kebocoran memori
    plt.close()
    

        
        
    
                
    
