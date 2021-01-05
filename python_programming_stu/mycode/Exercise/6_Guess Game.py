'''
 1 ~ 100 임의의 숫자를 맞추시오
'''
import random

print("1~100 임의의 숫자를 입력하세요")
user_input = int(input())

while True:
    guess_number = random.randint(1, 100)
    print(guess_number)

    if guess_number == user_input :
        print("같은 숫자가 나와 게임을 종료합니다.")
        break

    elif user_input > guess_number :
        print("숫자가 너무 큽니다.")

    else :
        print("숫자가 너무 작습니다.")




