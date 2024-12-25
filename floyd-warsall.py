# Hàm Floyd-Warshall
def floyd_warshall(graph):
    # Số lượng đỉnh trong đồ thị
    num_vertices = len(graph)

    # Khởi tạo khoảng cách ban đầu bằng trọng số trên đồ thị
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            dist[i][j] = graph[i][j]
    
    # Khoảng cách từ một đỉnh đến chính nó là 0
    for i in range(num_vertices):
        dist[i][i] = 0

    # Áp dụng thuật toán Floyd-Warshall
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Kiểm tra nếu tồn tại đường đi ngắn hơn thông qua k
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Ma trận trọng số của đồ thị (bảng khoảng cách)
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

# Tính toán ma trận khoảng cách ngắn nhất
result = floyd_warshall(graph)

# In kết quả
print("Ma trận khoảng cách ngắn nhất giữa các thành phố:")
for row in result:
    print(row)
