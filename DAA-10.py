# Kruskal's Algorithm

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal(vertices, edges):
    # Sort edges according to weight
    edges.sort(key=lambda x: x[2])

    parent = list(range(vertices))
    rank = [0] * vertices

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        x = find(parent, u)
        y = find(parent, v)

        # Add edge if it does not form a cycle
        if x != y:
            mst.append((u, v, weight))
            total_cost += weight
            union(parent, rank, x, y)

    print("Edges in Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "--", v, "=", weight)

    print("Minimum Cost:", total_cost)


# Number of vertices
vertices = 4

# Edges: (source, destination, weight)
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(vertices, edges)

