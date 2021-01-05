lang_dict = {}
lang_dict = dict()

# dict값을 저장
lang_dict[100] = '자바'
lang_dict[200] = '파이썬'
lang_dict[200] = '텐서플로'
lang_dict[300] = 'PyTorch'
print((lang_dict))

# dict에서 값을 읽기
print(lang_dict[300])
# print(lang_dict[400])
# KeyError: 400
value = lang_dict.get(400)
print(value)
if value :
    print(value)
else:
    print('해당 key의 값이 없음')


for k, v in lang_dict.items():
    print(k, v)

# key 찾기
print(200 in lang_dict)
# value 찾기
print('자바' in lang_dict.values())


# zip() 함수
days = ["월요일", "화요일", "수요일"]
fruits = ["사과", "바나나", "딸기"]
coffees = ["아메리카노", "라떼", "모카", "믹스"]

print(zip(days, fruits, coffees), type(zip(days, fruits, coffees)))
for day, fruit, coffee in zip(days, fruits, coffees):
    print(day, fruit, coffee)