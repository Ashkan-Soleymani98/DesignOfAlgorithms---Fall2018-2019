import sys
sys.setrecursionlimit(100000)

def dotFind(n):
    return pow(2, n + 1) - 1


def gradFind(a, b):
    if a[0] == b[0]:
        if a[1] < b[1]:
            return float('inf')
        else:
            return float('-inf')
    else:
        return (a[1] - b[1]) / (a[0] - b[0])


def findMostLeft(a):
    tempMin = a[0]
    tempI = 0
    for i, b in enumerate(a):
        if b < tempMin:
            tempMin = b
            tempI = i
    return tempI


def mapToTree(Xs, Ys, counts):
    global indices
    root = findMostLeft(Xs)

    rootX = Xs.pop(root)
    rootY = Ys.pop(root)

    countRoot = counts.pop(root)

    if len(Xs) == 2:
        indices[int(counts[0])] = 2 * indices[int(countRoot)]
        indices[int(counts[1])] = 2 * indices[int(countRoot)] + 1
        return

    grads = list()
    for i in zip(Xs, Ys):
        grads.append(gradFind([rootX, rootY], i))

    grads, Xs, Ys, counts = zip(*sorted(zip(grads, Xs, Ys, counts)))

    grads = list(grads)
    Xs = list(Xs)
    Ys = list(Ys)
    counts = list(counts)

    k = len(Xs) // 2

    indices[int(counts[findMostLeft(Xs[0:k])])] = 2 * indices[int(countRoot)]
    mapToTree(Xs[0:k], Ys[0:k], counts[0:k])

    indices[int(counts[k + findMostLeft(Xs[k:])])] = 2 * indices[int(countRoot)] + 1
    mapToTree(Xs[k:], Ys[k:], counts[k:])



n, k = map(int, input().split())

Xs = []
Ys = []

for i in range(n):
    a = list(map(int, input().split()))
    Xs.append(a[0])
    Ys.append(a[1])

for i in range(n - dotFind(k)):
    print(0)
    del Xs[0]
    del Ys[0]

indices = [0] * len(Xs)
counts = [i for i in range(len(Xs))]

root = findMostLeft(Xs)

indices[root] = 1

mapToTree(Xs, Ys, counts)
for i in indices:
    print(i)

