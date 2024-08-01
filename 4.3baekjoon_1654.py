k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]

def binary_search():
    result, bottom, top = 0, 1, max(array)

    while bottom <= top:
        cut = (bottom + top) // 2

        total = 0
        for a in array:
            if a >= cut:
                total += (a // cut)
    
        if total < n:
            top = cut - 1
        else:
            bottom = cut + 1
            result = cut

    return result

print(binary_search())