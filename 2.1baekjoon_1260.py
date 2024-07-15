from collections import deque

def dfs(v, visited):
    visited.add(v)
    print(v, end=' ')  

    for i in range(1, n + 1):
        if i not in visited and matrix[v][i] == 1:
            dfs(i, visited)

def bfs(start):
    queue = deque([start])
    visited = set([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if i not in visited and matrix[v][i] == 1:
                queue.append(i)
                visited.add(i)

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

visited_dfs = set()
dfs(v, visited_dfs)
print()  
bfs(v)
