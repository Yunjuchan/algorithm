def isyun(year) :
    year = int(year)
    if year % 400 == 0 :
        return 1
    elif year % 100 == 0 :
        return 0
    elif year % 4 == 0 :
        return 1
    return 0

def floated_days(year, month, day) :
    year = int(year)
    day = int(day)
    month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    month_days = [31, 28 + isyun(year), 31, 30, 
                  31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(len(month_list)) :
        if month == month_list[i] :
            return sum(month_days[:i]) + day - 1
date = input()
date = date.replace(',', '')
date = date.replace(':', ' ')
date= date.split()
total_minute = (365 + isyun(date[2])) * 24 * 60
floated_minute = floated_days(date[2], date[0], date[1]) * 24 * 60 + int(date[3]) * 60 + int(date[4])
print(floated_minute / total_minute * 100)
print(floated_days(date[2], date[0], date[1]))
 

## 파이썬에는 datetime이라는 라이브러리가 있는데 
## datetime 라이브러리에 들어있는 함수를 사용하면 간단하게 해결 가능

