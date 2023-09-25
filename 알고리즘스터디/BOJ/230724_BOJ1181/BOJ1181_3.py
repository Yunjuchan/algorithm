T = int(input())
word_list = []
for t in range(T) :
    if word_list == [] :
        word_list.append(input())
        continue
    new_word = input()
    for i in range(len(word_list)) :
        if new_word in word_list :
            break
        elif len(new_word) < len(word_list[i]) : 
            word_list.insert(i, new_word)
        elif len(new_word) == len(word_list[i]) :
            if new_word < word_list[i] :
                word_list.insert(i, new_word)
        if i == len(word_list) - 1 :
            word_list.insert(i+1, new_word)
            
            
        
print(*word_list, sep='\n')

# 시간 초과