import sys
input = sys.stdin.readline
T = int(input())
word_list = []
for t in range(T) :
    new_word = input().strip()
    word_list.append(new_word)
word_list = list(set(word_list))
# 정렬
word_list.sort()
for i in range(1, 51) :    
    for word in word_list :
        if len(word) == i :
            print(word)

# word_list.sort(key= lambda x :[len(x),x])


# sys를 통해 입력값 받고 시간단축 엄청 되었음

# set과 list 를 사용해 중복값 제거

# 정렬은 sort로 알파벳순 정렬 후
# 길이에 따라 출력될 수 있도록 실행

# sort의 인자로 key=가 있는데
# function을 통해 정렬 기준을 정할 수 있음
# sort(*iters, key= lambda x : len(x)) # 길이순으로 정렬
# sort(*iters, key= lambda x :(len(x),x)) # 길이순으로 정렬 후 알파벳순으로 정렬

# 합병정렬로 문제를 해결하는 풀이도 존재했음