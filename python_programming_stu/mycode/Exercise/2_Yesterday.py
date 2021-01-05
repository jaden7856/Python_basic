'''
 Yesterday.txt 파일 읽고
 yesterday 라는 단어가 몇번나왔는지
 YESTERDAY 라는 단어가 몇번나왔는지 yes.upper().count('YESTERDAY')
 Yesterday 라는 단어가 몇번나왔는지
'''


# fath = 'C:/Users/User/Desktop/DataStudy/Python/python_programming_stu/mycode/Exercise/yesterday.txt'

# file read를 함수로 선언
def file_read(file_name):
    with open(file_name, 'r') as file:
        yes = file.read()
        print(yes)
    return yes


yesterday_lyric = file_read('yesterday.txt')

print(yesterday_lyric.count('yesterday'))
print(yesterday_lyric.upper().count(('YESTERDAY')))
print(yesterday_lyric.count(('Yesterday')))
