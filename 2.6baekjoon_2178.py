from collections import deque
import sys
sys.setrecursionlimit(50000)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check_bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    dist[0][0] = 1

    while queue:
        x,y = queue.popleft()
        if x == N-1 and y == M-1:
            return dist[x][y]
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))
                dist[nx][ny] = dist[x][y]+1

    return -1
    
N, M =  map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dist = [[0]*M for _ in range(N)]
result=check_bfs()
print(result)