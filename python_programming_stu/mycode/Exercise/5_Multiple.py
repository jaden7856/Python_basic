'''
 구구단을 작성하세요
'''


while True:
    print("구구단 몇 단을 계산할까요(1~9)?")
    stage = int(input())

    if stage == 0 :
        print(' Good - Bye ')
        break
    elif stage <= 1 or stage > 10 :
        print(' 1 ~ 9 사이만 인정 ')
        continue

    for i in range(1, 10):
        print('{0} x {1} = {2}'.format(stage, i, stage*i))