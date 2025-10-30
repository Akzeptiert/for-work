import networkx as nx
import matplotlib.pyplot as plt

# 1. Данные: Координаты для расположения, рейсы для связей
city_pos = {
    'Москва': (37.6, 55.7),
    'Санкт-Петербург': (30.3, 59.9),
    'Новосибирск': (82.9, 55.0),
    'Екатеринбург': (60.6, 56.8),
    'Сочи': (39.7, 43.5)
}

flights = [
    ('Москва', 'Санкт-Петербург', 635),
    ('Москва', 'Екатеринбург', 1416),
    ('Москва', 'Новосибирск', 2811),
    ('Москва', 'Сочи', 1362),
    ('Санкт-Петербург', 'Сочи', 1920),
    ('Екатеринбург', 'Новосибирск', 1523)
]

# 2. Создание и наполнение графа
G = nx.Graph()
G.add_nodes_from(city_pos.keys())
G.add_weighted_edges_from(flights, weight='distance')

# 3. Отрисовка
plt.figure(figsize=(10, 7))

# Используем одну общую функцию draw() для основной отрисовки
nx.draw(G,
        pos=city_pos,
        with_labels=True,
        node_color='skyblue',
        node_size=700,
        font_weight='bold',
        font_family='Arial'
       )

# Отдельно добавляем подписи расстояний на ребра
edge_labels = nx.get_edge_attributes(G, 'distance')
nx.draw_networkx_edge_labels(G, pos=city_pos, edge_labels=edge_labels)

plt.title('Карта авиаперелетов')
plt.show()