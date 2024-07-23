def backtracking():
    if len(answer) == m:
        print(*answer)
        return

    check = 0
    for i in range(len(array)):
        if check != array[i] :
            answer.append(array[i])
            check = array[i]
            backtracking()
            answer.pop()

n, m = map(int, input().split())
array = []
for a in range(n):
    array.append(a+1)

answer = []

backtracking()