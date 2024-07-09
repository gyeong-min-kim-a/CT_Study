'''
1. n, k 입력
2. 큐 생성
3. WHILE문 반복
4. K번째만큼 시계반대방향으로 회전
5. 첫번째 요소 POP
'''


from collections import deque

n,k = map(int, input().split())

p = deque([i for i in range(1,n+1)])

r = []

while len(p) != 0:
    p.rotate(-k+1)
    r.append(p.popleft())

print("<" + str(r)[1:-1] + ">")