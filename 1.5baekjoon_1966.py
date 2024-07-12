def printQ(n, m, imp):
    sorted_imp = sorted(imp, reverse=True)
    imp_tuple = [(val, idx) for idx, val in enumerate(imp)]
    target = imp_tuple[m]

    c = 0 
    while [item[0] for item in imp_tuple] != sorted_imp: 
        max_value = sorted_imp[c]
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