n = int(input())
 
levels = list(map(int, input().split()))
levels.sort(reverse=True)
 
gold = 0

while len(levels) > 1:
    gold += levels[0] + levels[1]
    
    new_level = max(levels[0], levels[1])
    levels = [new_level] + levels[2:]

print(gold)