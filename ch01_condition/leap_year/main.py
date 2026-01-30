str_years = '윤년입니다.'
year = int(input('연도를 입력하세요 >>> '))
if int(year) % 400  == 0:
    str_years = '윤년입니다.'
elif int(year) % 100 == 0:
    str_years = '윤년이 아닙니다.'
elif int(year) % 4 == 0:
    str_years = '윤년입니다.'
else:
    str_years = '윤년이 아닙니다.'
print(str_years)

# 논리 연산자 사용한 풀이 방식
if year % 400 == 0 and (year % 4 == 0 or year % 100 != 0):
    print(f'{year} 년은 윤년입니다.')
else:
    print(f'{year} 년은 윤년이 아닙니다.')

# ch02_loops -> main_while / main_for