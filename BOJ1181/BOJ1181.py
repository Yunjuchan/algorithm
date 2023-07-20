T = int(input())
word = []

for t in range(T) :
    word.append(input())
    for i in range(1, len(word)) :
        for j in range(len(word)-i+1) :
            if len(word[j-1]) > len(word[j]) :
                word[j-1], word[j] = word[j], word[j-1]
            elif word[j-1] > word[j] :
                word[j-1], word[j] = word[j], word[j-1]
print(*word, sep='\n')

# 버블소트 사용 

# 시간초과 오류
