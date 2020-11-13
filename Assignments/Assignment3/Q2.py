n, m = map(int, input().split())

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

adjMat = [[0 for j in range(n + 2)] for i in range(n + 2)]

Cs = [As[i] - Bs[i] for i in range(n)]

movs = [[0 for j in range(n + 2)] for i in range(n + 2)]
for i in range(1, n + 1):
    movs[i][i] = adjMat[i][i]

limit = 0
for i, a in enumerate(Cs):
    if a < 0:
        adjMat[0][i + 1] = -a
    elif a > 0:
        adjMat[i + 1][n + 1] = a
        limit += a

for i in range(m):
    a, b = map(int, input().split())
    adjMat[a][b] = As[a - 1]
    adjMat[b][a] = As[b - 1]

graph = [[adjMat[i][j] for j in range(n + 2)] for i in range(n + 2)]


def BFS(root, dest):
    parents = [-1 for i in range(n + 2)]
    marked = [False for i in range(n + 2)]
    bfs(root, marked, parents, dest)
    return parents


def bfs(root, marked, parents, dest):
    queue = [root]
    parents[root] = -1
    while len(queue) > 0:
        u = queue.pop(0)
        marked[u] = True
        for v in range(n + 2):
            if not marked[v] and adjMat[u][v] > 0:
                queue.append(v)
                parents[v] = u
    return marked[dest]


maxFlow = 0
while True:
    parents = BFS(0, n + 1)
    if parents[n + 1] < 0:

        break

    pathFlow = 200
    v = n + 1
    while v != 0:
        u = parents[v]
        pathFlow = min(pathFlow, adjMat[u][v])
        v = u

    v = n + 1
    while v != 0:
        u = parents[v]
        adjMat[u][v] -= pathFlow
        adjMat[v][u] += pathFlow
        v = u

    maxFlow += pathFlow
    # print(adjMat)

if maxFlow >= limit:
    print("YES")
    outMat = [[max(0, graph[i][j] - adjMat[i][j]) for j in range(n + 2)] for i in range(n + 1)]
    for i in range(1, n + 1):
        temp = 0
        for j in range(1, n + 1):
            if j != i:
                temp += outMat[i][j]
        outMat[i][i] = As[i - 1] - temp
    for i in range(1, n + 1):
        print(*outMat[i][1:n + 1])
else:
    print("NO")

