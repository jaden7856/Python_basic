'''
 나이 = 현재년도 - 태어난 년도 + 1
 태어난 년도를 input()
'''

from datetime import datetime as dt
# 현재년도 datetime 클래스에 선언된 today() 매서드를 호출
current_year = dt.today().year
print("태어난 년도를 입력하세요")
birth = int(input())
age = current_year - birth + 1

if 17 <= age < 20 :
    print("고등학생입니다.")
elif 20 <= age < 27 :
    print("대학생입니다.")
else :
    print("학생이 아닙니다.")