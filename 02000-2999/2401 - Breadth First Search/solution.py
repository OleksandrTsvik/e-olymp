from collections import deque

n, s, f = list(map(int, input().split()))  # Считываем числа через пробел
A = [list(map(int, input().split())) for i in range(n)]  # зчитуємо матрицю суміжності

dist = [0] * n  # Список расстояний до вершин
s -= 1
f -= 1
dist[s] = 0  # До стартовой вершины расстояние 0
queue = deque([s])  # Создаём очередь из начальной вершины

while len(queue) > 0:
    top = queue.popleft()  # Извлекаем первую вершину из очереди

    if top == f:  # Если мы дошли до конечной вершины, выводим расстояние до неё
        print(dist[f])
        exit(0)
    else:
        for i in range(n):  # Добавляем соседей данной вершины, которых ещё нет в очереди
            if A[top][i] == 1 and dist[i] == 0:
                queue.append(i)
                dist[i] = dist[top] + 1

print(dist[f])
