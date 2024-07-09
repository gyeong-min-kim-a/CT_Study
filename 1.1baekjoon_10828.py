# 입출력 모듈 
import sys

input = sys.stdin.readline
output = sys.stdout.write


# 스택 클래스 구현
class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0: 
            return -1
        else:
            return self.items.pop()

    def size(self):
        return(len(self.items))
    
    def empty(self):
        if len(self.items) == 0:
            return 1
        else :
            return 0
    
    def top(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[-1]
        

# 명령의 수 
total_cnt = int(input().rstrip())
stk = stack()

# 스택 클래스 사용
result = []

for cnt in range(total_cnt):

    command = input().rstrip( ).split()

    if command[0] == 'push':
        n = command[1]
        stk.push(n)
    elif command[0] == 'pop':
        result.append(f"{stk.pop()}\n")
    elif command[0] == 'size':
        result.append(f"{stk.size()}\n")
    elif command[0] == 'empty':
        result.append(f"{stk.empty()}\n")
    elif command[0] == 'top':
        result.append(f"{stk.top()}\n")

output(''.join(result))