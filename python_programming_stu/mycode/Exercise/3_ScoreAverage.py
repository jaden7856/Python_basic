'''
 이차원 리스트에서 사람별 평균을 구하자
'''
import numpy
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]

midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
idx = 0

for subject in midterm_score:
    # 학생별 과목합계 점수를 계산
    for score in subject :
        # 학생별로 과목 점수를 저장
        student_score[idx] += score
        idx += 1
    # 과목이 바뀔 때 학생 인덱스 초기화
    idx = 0
else:
    print(f"학생별 합계 점수 : {student_score}")
    A, B, C, D, E = student_score
    student_average = [A/3, B/3, C/3, D/3, E/3]

print(f"A학생 평균 : {round(student_average[0])}\nB학생 평균 : {round(student_average[1])}\n"
      f"C학생 평균 : {round(student_average[2])}\nD학생 평균 : {round(student_average[3])}\n"
      f"E학생 평균 : {round(student_average[4])}")
