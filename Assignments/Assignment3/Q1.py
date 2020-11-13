n, m, d = map(int, input().split())

corpseCites = list(map(int, input().split()))
corpseCites = [i - 1 for i in corpseCites]

temp = [False for i in range(n)]
for i in corpseCites:
    temp[i] = True
isCorpseCites = temp

adjList = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    adjList[a].append(b)
    adjList[b].append(a)


def BFS(root, dist):
    marked = [False for i in range(n)]
    bfs(root, marked, dist)


def bfs(root, marked, dist):
    queue = [root]
    dist[root] = 0
    while len(queue) > 0:
        u = queue.pop(0)
        marked[u] = True
        for i in adjList[u]:
            if not marked[i]:
                queue.append(i)
                dist[i] = dist[u] + 1
    return


dist1 = [-1 for i in range(n)]
BFS(0, dist1)
startMaxPath = -1
startMaxPathDist1 = 0
for i in corpseCites:
    if dist1[i] > startMaxPathDist1:
        startMaxPath = i
        startMaxPathDist1 = dist1[i]

dist2 = [-1 for i in range(n)]
BFS(startMaxPath, dist2)
endMaxPath = -1
endMaxPathDist1 = 0
for i in corpseCites:
    if dist2[i] > endMaxPathDist1:
        endMaxPath = i
        endMaxPathDist1 = dist2[i]

# print(dist2)
# print(endMaxPath)

dist3 = [-1 for i in range(n)]
BFS(endMaxPath, dist3)

# print(dist2)
# print(dist3)

counter = 0
for i in range(n):
    if dist2[i] <= d and dist3[i] <= d:
        counter += 1

print(counter)
