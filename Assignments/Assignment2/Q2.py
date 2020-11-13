n, p = map(int, input().split())

par = [-1 for i in range(n)]


def find(x):
    if par[x] < 0:
        return x
    par[x] = find(par[x])
    return par[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if par[x] < par[y]:
        x, y = y, x
    par[y] += par[x]
    par[x] = y

As = list(map(int, input().split()))
Xors = list()

for i in range(n):
    for j in range(i + 1, n):
        Xors.append([As[i] ^ As[j], i, j])

Xors = sorted(Xors, reverse=True)
# print(Xors)

lastEdge = Xors[0][0]
for i in Xors:
    if find(i[1]) != find(i[2]):
        union(i[1], i[2])
        lastEdge = i[0]

print(lastEdge)
