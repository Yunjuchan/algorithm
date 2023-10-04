from collections import deque
tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
N = len(tickets)
tickets.sort()
dic = {}
answer = ["ICN"]
que = deque()
for s, e in tickets :
    x = dic.get(s, deque())
    x.append(e)
    dic[s] = x
    dic[e] = dic.get(e, deque())
x = dic["ICN"].popleft()
que.append(x)
while que :
    x = que.popleft()
    if len(answer) == N :
        answer.append(x)
        break
    answer.append(x)
    if not dic[x]:
        answer.pop()
        pre = answer[-1]
        answer.pop()
        dic[pre].append(x)
        que.append(pre)
        continue
    y = dic[x].popleft()
    que.append(y)
print(answer)