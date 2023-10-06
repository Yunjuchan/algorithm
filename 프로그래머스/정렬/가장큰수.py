from collections import deque
numbers = [3, 30, 34, 5, 9]
def solution(numbers):
    numbers.sort(reverse=True)
    numbers = list(map(str, numbers))

    # 999 99 9 998 997 996 995 994 993 992 991 990 989 988 98 987 986 985 984 983 982 981 980 979 978 977 97 976 이런식으로 진행됨
print(solution(numbers))