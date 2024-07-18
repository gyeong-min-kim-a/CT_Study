import sys
sys.setrecursionlimit(50000) 

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check_dfs(x, y, cnt):
    if not (0 <= x < M and 0 <= y < N):
        return cnt
    if graph[x][y] == 1 and not visited[x][y]:
        cnt += 1
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cnt = check_dfs(nx, ny, cnt)
    return cnt


num = int(input()) 
for _ in range(num):
    M, N, K = map(int, input().split())  
    graph = [[0] * N for _ in range(M)] 
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    clusters = []
    visited = [[False] * N for _ in range(M)] 
    for x in range(M):  
        for y in range(N):
            if graph[x][y] == 1 and not visited[x][y]:
                cnt = check_dfs(x, y, 0)
                clusters.append(cnt)
    print(len(clusters))