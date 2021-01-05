'''
 책 목록 만들기
'''

books = list()

books.append({'제목': '개발자의 코드', '출판연도': '2013.02.28', '출판사': 'A출판', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린 코드', '출판연도': '2013.03.04', '출판사': 'B 출판 ', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A출판 ', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판연도': '2010.02.10', '출판사': 'B출판 ', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판연도': '2013.12.12', '출판사': 'C출판 ', '쪽수': 248, '추천유무': True})

all_page_sum_value = int()

page = [book["제목"] for book in books if book['쪽수'] > 250]
recommend = [book["제목"] for book in books if book['추천유무']]
all_page_sum_value = sum([book["쪽수"] for book in books])
company = set([book["출판사"].replace(" ", '') for book in books])

print('쪽수가 250쪽 넘는 책 리스트 : ', page)
print('추천하는 책 리스트 : ', recommend)
print('출판사 목록 : ', company)