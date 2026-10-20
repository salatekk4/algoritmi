edges = [
    (1, 2, 2), (1, 4, 4), (1, 7, 6),
    (2, 3, 1), (2, 4, 1), (2, 5, 2), (2, 8, 8),
    (3, 5, 7),
    (4, 6, 5), (4, 7, 1),
    (5, 7, 2), (5, 8, 2),
    (6, 7, 1),
    (7, 8, 2)
]
n = 8  


# 1. Алгоритм Прима 
visited = [1]
prim_tree = []
prim_weight = 0

while len(visited) < n:
    best_edge = None
    min_w = 999999

    for u, v, w in edges:
        u_in = u in visited
        v_in = v in visited

        if (u_in and not v_in) or (v_in and not u_in):
            if w < min_w:
                min_w = w
                best_edge = (u, v, w)

    u, v, w = best_edge
    prim_tree.append(best_edge)
    prim_weight += w

    if u not in visited:
        visited.append(u)
    if v not in visited:
        visited.append(v)

print("=== Алгоритм Прима ===")
print("Суммарный вес:", prim_weight)
for u, v, w in prim_tree:
    print(f"Ребро ({u}, {v}) с весом {w}")


# 2. Алгоритм Краскала 
sorted_edges = sorted(edges, key=lambda x: x[2])

group = {i: i for i in range(1, n + 1)}

kruskal_tree = []
kruskal_weight = 0

for u, v, w in sorted_edges:
    if group[u] != group[v]:
        kruskal_tree.append((u, v, w))
        kruskal_weight += w

        old_group = group[v]
        new_group = group[u]
        for node in range(1, n + 1):
            if group[node] == old_group:
                group[node] = new_group

        if len(kruskal_tree) == n - 1:
            break

print("\n=== Алгоритм Краскала ===")
print("Суммарный вес:", kruskal_weight)
for u, v, w in kruskal_tree:
    print(f"Ребро ({u}, {v}) с весом {w}")
