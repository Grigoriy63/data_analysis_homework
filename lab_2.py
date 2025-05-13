import networkx as nx
import matplotlib.pyplot as plt

"""
Задание:
Требуется получить центральность для 15 узлов «горкой», т.е. с ростом в центре списка значений и опусканием на края
"""
G = nx.Graph()

# Добавляем узлы
G.add_nodes_from(range(15))

G.add_edges_from([
    (7, 6), (7, 8),
    (6, 5), (8, 9),
    (5, 4), (9, 10),
    (4, 3), (10, 11),
    (3, 2), (11, 12),
    (2, 1), (12, 13),
    (1, 0), (13, 14)
])

# Вычисляем центральность
centrality = nx.eigenvector_centrality(G, max_iter=1000)

# Сортируем по узлам
sorted_centrality = [centrality[i] for i in range(15)]

for i, val in enumerate(sorted_centrality):
    print(f"Узел {i}: {val:.4f}")


plt.figure(figsize=(10, 5))
plt.plot(range(15), sorted_centrality, marker='o')
plt.title("Центральность для графика 'горкой'")
plt.xlabel("Узлы")
plt.ylabel("Центральность")
plt.grid(True)
plt.show()
