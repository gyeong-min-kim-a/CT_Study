def solution(n, times):
    front, rear = 1, max(times) * n
    answer = rear

    while front <= rear:
        mid = (front + rear) // 2
        print(mid)
        total = sum(mid // time for time in times)

        if total >= n:
            answer = mid
            rear = mid - 1
        else:
            front = mid + 1

    return answer
