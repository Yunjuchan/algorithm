S = list(input())
cnt = 1
for i in range(len(S)-1) :
    if S[i] != S[i+1] :
        cnt += 1
print(cnt // 2)