
# 윤년인지 확인하는 함수 400으로 나누어지면 윤년 
# 400으로 안나뉘어지고 100으로 나뉘어지면 평년
# 위의 조건을 만족하지 않고 4로 나누어지면 윤년
# 나머지 해는 평년
def is_yun(year) :
    if year % 400 == 0 :
        return 1
    elif year % 100 == 0 :
        return 0
    elif year % 4 == 0 :
        return 1
    else :
        return 0
    
# 1월 1일부터 몇일이 지났는지 확인하는 함수
# month_days : 각 달이 몇일까지 있는지 저장
# accu_days : 각 달의 말일까지 날짜를 셋을 때 지난 일 수 
def date_count(y, m, d) :
    cnt = 0
    month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    accu_days = [0] * 13
    # 누적합 계산
    for i in range(1,13) :
        accu_days[i] = accu_days[i-1] + month_days[i]
    # 1월 1일부터 지난 날의 수 계산
    # 전달의 마지막날 까지 더한 일 수
    if is_yun(y) == 1 and m > 2 :
        cnt = accu_days[m-1] + 1 
    else :
        cnt = accu_days[m-1]
    # 이번달 더하기
    cnt += d
    return cnt
# 남은날 구하기
def res_days_count(date1, date2) :
    y1 = date1[0]
    y2 = date2[0]
    res_days = 0
    while y1 < y2 :
        if is_yun(y1) == 1 :
            res_days += 366
        else :
            res_days += 365
        y1 += 1
    res_days = res_days - date_count(*date1) + date_count(*date2)
    print(f'D-{res_days}')

today = list(map(int, input().split()))
end_day = list(map(int, input().split()))

# 구현 1001년 이상 차이나면 gg
# 1000년 차이나는데 끝나는 달이 더 크면 gg
# 달이 같으면 날이 더 크거나 같을때 gg
# 나머지는 남은 날 계산해주는 함수 호출
if end_day[0] - today[0] > 1000 :
    print('gg')
elif end_day[0] - today[0] == 1000 :
    if end_day[1] > today[1] :
        print('gg')
    elif end_day[1] == today[1] :
        if end_day[2] >= today[2] :
            print('gg')
        else :
            res_days_count(today, end_day)
    else :
        res_days_count(today, end_day)
else :
    res_days_count(today, end_day)