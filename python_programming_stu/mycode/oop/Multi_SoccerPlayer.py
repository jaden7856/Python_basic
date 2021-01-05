# 선수명, 선수 포지션, 선수 등번호
names = ['손흥민', '박지성', '조현재', '메시']
positions = ['DF', 'FW', 'MF', 'GK']
back_numbers = [7, 10, 11, 6]

# Class 없이 여러명의 선수를 2차원 배열에 저장
for na, po, ba in zip(names, positions, back_numbers):
    print(na, po, ba)

players = [[name, posiotn, back_number] for name, posiotn, back_number in zip(names, positions, back_numbers)]
print(players)

# back_number 를 변경
player1 = players[0]
player1[2] = 20
print(player1)

# SoccerPlayer 클래스를 import
from python_programming_stu.mycode.oop.python_class import SoccerPlayer

player = SoccerPlayer('dooly', 'MF', 10)
print(player)
players_obj = [SoccerPlayer(name, position, back_number)
               for name, position, back_number in zip(names, positions, back_numbers)]

# back_number 를 변경
player1 = players_obj[0]
player1.change_back_number(30)
print(player1)
