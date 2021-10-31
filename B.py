# 標準入力を受け付ける。
N = int(input())

# edges[各頂点] = [各頂点と辺で結ばれる頂点1, 各頂点と辺で結ばれる頂点2, ...]で管理する。
# edges[0]は利用しない。
edges = []
for _ in range(N + 1):
    edges.append([])

for _ in range(N - 1):
    A, B = map(int, input().split())
    # 辺の情報からedgesへ値を代入する。
    edges[A].append(B)
    edges[B].append(A)

for edge in edges:
    # 各頂点に対し、スターであるか確かめる。
    if len(edge) == N - 1:
        print('Yes')
        exit()

print('No')
