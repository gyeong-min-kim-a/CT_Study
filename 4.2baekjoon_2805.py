n, m = map(int, input().split())
array = list(map(int, input().split()))

def binary_search():
    bottom, top = 0, max(array)
    result = 0
    
    while bottom <= top:
        cut = (bottom + top) // 2
        total = 0
        
        for a in array:
            if a > cut:
                total += a - cut
        
        if total == m:
            return cut
        elif total < m:
            top = cut - 1
        else:
            bottom = cut + 1
            result = cut
    
    return result

print(binary_search())