from python_programming_stu.mycode.Exercise.Fahrenheit import *


print("섭씨 온도를 입력하세요")
Cel = input()

#fah = ((9/5) * float(Cel)) + 32
fah = TempConvert(Cel)

print("섭씨온도 :", Cel)
# print("화씨온도 :", round(fah, 2))
print("화씨온도 {:.2f}".format(fah))
print(sayHello('파이썬'))