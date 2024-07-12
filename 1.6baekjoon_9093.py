def reversing(sentenct):
    for word in sentence:
        each_word_list = list(word)
        reverse_word = []
        for i in range(len(each_word_list), 0, -1):
            reverse_word.append(each_word_list[i-1])
        print(''.join(reverse_word), end=' ')
    print()
    
num = int(input())
for _ in range(num):
    sentence = input().split()
    reversing(sentence)