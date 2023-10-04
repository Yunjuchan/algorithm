from collections import deque
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
def solution(tickets):
    N = len(tickets)
    tickets.sort()
    dic = {}
    dic2 = {}
    answer = []
    for s, e in tickets :
        x = dic.get(s, [])
        x2 = dic2.get(s, [])
        x.append(e)
        x2.append(False)
        dic[s] = x
        dic2[s] = x2
        
    def dfs(now, level, path) :
        nonlocal answer
        if answer : return
        if level == N+1 :
            answer = path
            return 
        if not dic.get(now, []) : return
        for i in range(len(dic[now])) :
            if dic2[now][i] : continue
            dic2[now][i] = True
            dfs(dic[now][i], level+1, path+[dic[now][i]])
            dic2[now][i] = False
    dfs("ICN", 1, ["ICN"])
    return answer

print(solution(tickets))