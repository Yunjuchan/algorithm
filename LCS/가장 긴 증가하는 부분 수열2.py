# boj 12015
N = int(input())
arr = list(map(int, input().split()))
C = [1] * N

def partition(arr) :
    mid = (start + end) // 2
    start = 0
    end = N-1
    left = partition(arr)