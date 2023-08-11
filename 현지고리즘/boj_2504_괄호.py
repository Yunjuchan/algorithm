from collections import deque
word = deque(input())
level_list = [[] for _ in range(16)] 
stack = []
tmp_list = [0] * 16
flag = 1

def push(char) :
    global flag
    level = len(stack)
    if level > 15 :
        flag = 0
        return
    stack.append(char)
    if char == '(' :     
        level_list[level].append(2)
    else :
        level_list[level].append(3)

def out(char) :
    global flag
    level = len(stack) - 1
    if level == -1 :
        flag = 0
        return
    if char == ')' :
        if stack[level] != '(' :
            flag = 0
            return
        stack.pop()
        x = level_list[level].pop()
        if tmp_list[level+1] :
            tmp_list[level] += x * tmp_list[level+1]
            tmp_list[level+1] = 0
        else :
            tmp_list[level] += x
    else :
        if stack[level] != '[' :
            flag = 0
            return
        stack.pop()
        x = level_list[level].pop()
        if tmp_list[level+1] :
            tmp_list[level] += x * tmp_list[level+1]
            tmp_list[level+1] = 0
        else :
            tmp_list[level] += x
    
while word :
    level = len(stack)
    char = word.popleft()

    if char == '[' or char == '(' :
        push(char)
    else :
        out(char)
    if flag == 0 :
        break
if len(stack) > 0 :
    flag = 0
    

if flag == 0 :
    print(0)
else :
    print(tmp_list[0])