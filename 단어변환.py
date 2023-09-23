from collections import deque
def diff_count(a, b) :
    cnt = 0
    for i in range(len(a)) :
        if a[i] != b[i] :
            cnt += 1
    return cnt
    
def solution(begin, target, words):
    n = len(words)
    words_adj = [[] for _ in range(n+1)]
    visited = [False]*n
    que = deque()
    que.append([0,[0,begin]])
    for i in range(n) :
        if diff_count(begin, words[i]) == 1 :
            words_adj[0].append([i+1, words[i]])
    for i in range(n) :
        for j in range(n) :
            if i == j : continue
            if diff_count(words[i], words[j]) == 1 :
                words_adj[i+1].append([j+1,words[j]])
                
    while que :
        level, now = que.popleft()
        for next in words_adj[now[0]] :
            if not visited[next[0]-1] :
                visited[next[0]-1] = True
                que.append([level+1, next])
                if next[1] == target :
                    return level+1
    return 0
begin = "hit"	
target = "cog"	
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))