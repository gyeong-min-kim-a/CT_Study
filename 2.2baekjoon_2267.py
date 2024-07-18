dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs_check(x,y, cluster_cnt):
    if not (0<=x<size and 0<=y<size):
        return cluster_cnt
    if graph[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        cluster_cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cluster_cnt = dfs_check(nx,ny, cluster_cnt)
    return cluster_cnt


size = int(input())
graph = []
for i in range(size):
    graph.append(list(map(int, input())))

visited = [[False] * len(graph[0]) for _ in range(len(graph))]
clusters = []

for x in range(size) :
    for y in range(size) :
        if graph[x][y] == 1 and not visited[x][y]:
            cluster_cnt = dfs_check(x,y, 0)
            clusters.append(cluster_cnt)
cluster_sorted = sorted(clusters)
print(len(cluster_sorted))
for c in cluster_sorted:
    print(c)

''' 입출력 예시
# 그래프 입력 
input_list = ['0110100', '0110101', '1110101', '0000111', '0100000', '0111110', '0111000']
size = len(input_list)

matrix = []
for num in input_list:
    matrix.append([int(char) for char in num])
# print(f'원본 메트릭스 {matrix}')
'''