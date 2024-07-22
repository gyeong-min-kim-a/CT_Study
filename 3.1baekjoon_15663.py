def backtracking():
    if len(answer) == m:
        print(*answer)
        return

    check = 0
    for i in range(len(array)):
        if check != array[i] and not visited[i]:
            answer.append(array[i])
            visited[i] = True
            check = array[i]
            backtracking()
            answer.pop()
            visited[i] = False

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

visited = [False] * len(array)  
answer = [] 

backtracking()