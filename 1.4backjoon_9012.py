def check_vps(input):
    input_, stack = list(input), []
        
    for i in input_:
        if i == '(':stack.append(i);
        elif i == ')' : 
            if len(stack)==0:
                stack.append(')') 
            elif stack[-1] == ')' :
                stack.append(')') 
            else:
                try:stack.pop();
                except IndexError:pass

    if len(stack) == 0:print('YES'); 
    else :print('NO')

number = int(input())
for i in range(number):
    in_ps = input()
    check_vps(in_ps)