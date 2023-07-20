T = int(input())
word_list = []

for t in range(T) :
    for i in range(len(word_list)) :
        new_word = input()
        if len(new_word) > len(word_list[i]) :
            continue 
        elif new_word > word_list[i] :
            continue
        word_list.insert(i+1, new_word)
print(*word_list, sep='\n')

# 시간초과 오류
