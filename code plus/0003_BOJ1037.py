div = int(input())
div_all = list(map(int, input().split()))
div_all.sort()
print(div_all[0] * div_all[-1])

## 약수를 정렬하고 앞과 뒤를 곱했을 때 원래의 수가 나오므로
## 0번 인덱스와 마지막 인덱스를 곱함