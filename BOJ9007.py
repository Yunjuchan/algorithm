import sys
input = sys.stdin.readline

# T = int(input())
K, N = map(int, input().split())
all_student = [] 
for i in range(4) :
    x = list(map(int, input().split()))
    for i in range(len(x)) :
        all_student.append([i, x[i]])
all_student.sort(key=lambda x : x[1])
print(all_student)
all_weight = 0
s1 = 0; s2 = 1; s3 = 2; s4 = 3
while True :
    pass
    
