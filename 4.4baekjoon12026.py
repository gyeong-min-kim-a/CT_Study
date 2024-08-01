def dynamic_programing(N, blocks):
    dp = [float('inf')] * N
    dp[0] = 0 

    order = 'BOJ'
    
    for i in range(N):
        current_char = blocks[i]
        next_char = order[(order.index(current_char) + 1) % 3]
        for j in range(i + 1, N):
            if blocks[j] == next_char:
                jump_cost = (j - i) ** 2
                dp[j] = min(dp[j], dp[i] + jump_cost)
    
    return dp[-1] if dp[-1] != float('inf') else -1

N = int(input())
blocks = input().strip()

print(dynamic_programing(N, blocks))