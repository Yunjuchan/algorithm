T = int(input())
word_list = []

for t in range(T) :
    if word_list == [] :
        word_list.append(input())
        continue
    for i in range(len(word_list)) :
        new_word = input()
        if len(new_word) < len(word_list[i]) : 
            word_list.insert(i, new_word)
        elif new_word < word_list[i] :
            word_list.insert(i, new_word)
print(*word_list, sep='\n')

# 시간초과 오류
