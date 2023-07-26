def is_yun(year) :
    if year % 400 == 0 :
        return 1
    elif year % 100 == 0 :
        return 0
    elif year % 4 == 0 :
        return 1
    else :
        return 0
def date_count(year, month, day) :
    cnt = 0
    if month > 11 :
        cnt += 334
    elif month > 10 :
        cnt += 304
    elif month > 9 :
        cnt += 273
    elif month > 8 :
        cnt += 243
    elif month > 7 :
        cnt += 212
    elif month > 6 :
        cnt += 181
    elif month > 5 :
        cnt  += 151
    elif month > 4 :
        cnt += 120
    elif month > 3 :
        cnt += 90
    elif month > 2 :
        cnt += 59
    elif month > 1 :
        cnt += 31
    if is_yun(year) == 1 and month > 3 :
        cnt += 1
    cnt += day
    return cnt

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

date1 = list(map(int, input().split()))
date2 = list(map(int, input().split()))

if date2[0] - date1[0] > 1000 :
    print('gg')
elif date2[0] - date1[0] == 1000 :
    if date1[1] < date2[1] :
        print('gg')
    elif date1[1] == date2[1] :
        if date1[2] <= date2[2] :
            print('gg')
        else : res_days_count(date1, date2)
    else : res_days_count(date1, date2)

else :
    res_days_count(date1, date2)


## 이유 모름 계속 오류남