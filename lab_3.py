import networkx as nx
import matplotlib.pyplot as plt


def generate_and_plot(n, p, seed=None):
    """
    Вычисляем грав в модели Эрдёша-Реньи
    Параметры по заданному варианту n=42, p=0,65
    """
    G = nx.erdos_renyi_graph(n, p, seed=seed)

    degrees = [deg for _, deg in G.degree()]
    avg_empirical = sum(degrees) / n
    avg_theoretical = (n - 1) * p

    print(f"Параметры для заданного варианта: n = {n}, p = {p}")
    print(f"Полученая средняя степень: {avg_empirical:.4f}")
    print(f"По формуле из лекции: {avg_theoretical:.4f}")

    # визуализация графа
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=seed)
    nx.draw_networkx_nodes(G, pos,
                           node_size=100,
                           node_color='skyblue',
                           edgecolors='black')
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.title(f"Визуализация графа, который получился")
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    generate_and_plot(n=42, p=0.65, seed=42)
