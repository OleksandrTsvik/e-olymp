from collections import deque

n, x = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

x -= 1
dist = [0 for i in range(n)]
visited = [False for i in range(n)]
q = deque([x])

while len(q) > 0:
    top = q.popleft()
    visited[top] = True

    for i in range(n):
        if a[top][i] == 1 and not visited[i] and dist[i] == 0:
            q.append(i)
            dist[i] = dist[top] + 1

for i in range(len(dist)):
    if not visited[i]:
        dist[i] = -1

print(*dist)
