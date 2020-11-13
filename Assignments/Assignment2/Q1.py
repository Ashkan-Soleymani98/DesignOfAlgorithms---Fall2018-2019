import sys
sys.setrecursionlimit(10000)
n, m = map(int, input().split())

edges = list()
for i in range(m):
    edges.append(list(map(int, input().split())))

# print(edges)


adjList = [[] for i in range(m)]
# marked = [False for i in range(m)]
place = [None for i in range(m)]


def checkIntersect(a, b):
    if a[0] < b[0] < a[1] < b[1] or a[1] < b[0] < a[0] < b[1] \
            or a[0] < b[1] < a[1] < b[0] or a[1] < b[1] < a[0] < b[0] \
            or b[0] < a[0] < b[1] < a[1] or b[0] < a[1] < b[1] < a[0] \
            or b[1] < a[0] < b[0] < a[1] or b[1] < a[1] < b[0] < a[0]:
        return True
    return False


for i in range(m - 1):
    for j in range(i + 1, m):
        if checkIntersect(edges[i], edges[j]):
            adjList[i].append(j)
            adjList[j].append(i)

# print(adjList)


def dfs(node, parentPlace):
    if place[node] is not None:
        if parentPlace == place[node]:
            return False
        else:
            return True
    place[node] = 1 if parentPlace == 2 else 2
    for u in adjList[node]:
        if not dfs(u, place[node]):
            return False
    return True


def DFS():
    for i in range(m):
        if place[i] is None:
            if not dfs(i, None):
                return False
    return True


if DFS():
    string = ""
    for i in place:
        if i == 1:
            string += 'O'
        else:
            string += 'I'
    print(string)
else:
    print("Impossible")

