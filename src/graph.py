import networkx as nx 
import matplotlib.pyplot as plt

def create_graph (edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()

    if edges:
        G.add_edges_from(edges)
    
    node = set(angka for pasangan in edges for angka in pasangan)
    
    for i in node:
        G.add_node(i)
        
    print(G)
    return G
    
def get_degree(G: nx.Graph, node: int) -> int:
    if node in G:
        degrees = G.degree(node)
        print(degrees)
        return degrees
    else:
        print('tidak ada node itu')
        return 0
    
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    visited = set()
    result = []
    
    def visit(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in G.neighbors(node):
                visit(neighbor)
    
    if start in G:
            visit(start)
            
    print(result)
    return result

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    visited = set()
    result = []
    queue = []
    
    if start in G:
        # Inisialisasi dengan node awal
        queue.append(start)
        visited.add(start)
        
        while queue:
            # Dequeue node dari depan queue
            current = queue.pop(0)
            result.append(current)
            
            # Tambahkan semua tetangga yang belum dikunjungi ke queue
            for neighbor in G.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    print(result)
    return result

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    try:
        return nx.shortest_path(G, source=source, target=target)
    except nx.NetworkXNoPath:
        return []  # Mengembalikan list kosong jika tidak ada jalur
    except nx.NodeNotFound:
        raise ValueError("Salah satu atau kedua simpul tidak ditemukan dalam graf")
        
def visualize_graph(G: nx.Graph) -> None:
    plt.figure(figsize=(8, 6))
    
    # Menentukan posisi node
    pos = nx.spring_layout(G)
    
    # Menggambar graf
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', 
            node_size=2000, font_size=12, font_weight="bold")

    # Simpan gambar
    plt.savefig("graph_visualization.png", format="png")
    
    # Tampilkan graf
    plt.show()
    

        
        
    
                
    