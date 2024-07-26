from itertools import combinations

vowels = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())
array = sorted(list(map(str, input().split())))

'''
backtracking 부분을 메소드로 구현하면 한줄이다.. ㅎㅎ
array_com = list(combinations(array, l))
'''
answer = []
array_com = []

def backtracking(start):
    if len(answer) == l:
        array_com.append(answer[:])  # 리스트의 복사본을 추가합니다.
        return
    for i in range(start, len(array)):
        answer.append(array[i])
        backtracking(i + 1)
        answer.pop()

backtracking(0)



result = []
for item in array_com:
    num_vowels = sum(1 for char in item if char in vowels)
    num_consonants = l - num_vowels

    if num_vowels >= 1 and num_consonants >= 2:
        result.append(item)

for item in result:
    print(*item, sep='')
# a t c i s w