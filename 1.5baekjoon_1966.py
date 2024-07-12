def printQ(n, m, imp):
    imp_tuple = [(val, idx) for idx, val in enumerate(imp)]
    target = imp_tuple[m]
    sorted_imp_tuple = sorted(imp_tuple, key=lambda x: x[0], reverse=True)

    c = 0 
    sotred_imp = [item[0] for item in sorted_imp_tuple] # 정렬을 확인하기 위해서 + 수정되지 않는 것이기 때문에, 변수를 만들어 저장

    while [item[0] for item in imp_tuple] != sotred_imp: # 입력된 순열이 정렬된 순열과 같을때까지
        max_value = sorted_imp_tuple[c][0] # 가장 큰 수는 정렬된 C번째
        if imp_tuple[c][0] < max_value:
            imp_tuple.append(imp_tuple[c])
            del imp_tuple[c]
        else:c += 1

    order = next(idx + 1 for idx, item in enumerate(imp_tuple) if item == target)
    print(order)

number = int(input())
for i in range(number):
    n,m = map(int, input().split())
    importance = list(map(int, input().split()))
    printQ(n,m,importance)