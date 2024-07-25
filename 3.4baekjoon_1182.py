def backtracking(start):
    if len(answer) == m:
        if sum(answer) == s:
            result.append(answer[:])
            return 

    for i in range(start, len(setting)):
        answer.append(setting[i])
        backtracking(i + 1)
        answer.pop()

n, s = map(int, input().split())
setting = list(map(int, input().split()))
result, answer = [], []

for m in range(1,n+1):
    backtracking(0)
print(len(result))