greet = 'Hello' * 4 + '\n'
end = 'Good\tbye'
print(greet + end)

is_flag = True
my_str = 'True'
print(type(is_flag), type(my_str))
greeting = "Hello World"
# c언어 스타일
print("파이썬 %s" % greeting)
print("파이썬 %i" % len(greeting))

print('문자열 길이 {}, 0번째 인덱스 값은 {}'.format(len(greeting), greeting[0]))
# 3.6 버전이후
print(f'문자열 길이 {len(greeting)}, 1번째 인덱스 값은 {greeting[1]}')

# 문자열 인덱스 슬라이싱
print(f"greeting[0:5] = {greeting[0:5]}") # 01234
print(f"greeting[6:11] = {greeting[6:11]}") # 678910
print(f"greeting[6:] = {greeting[6:]}") # 6이후부터
print(f"greeting[:5] = {greeting[:5]}") # 5이전
print(greeting, greeting[:])
print(greeting[::2])
print(greeting[::-1])

# 문자열 여러가지 함수
word = 'Good manufacturing Practice Good'
print(f'대문자로 변환 = {word.upper()}')
res = word.upper()
print(word,'\t',res)
print(f'소문자로 변환 = {word.lower()}')

print(word.title())
print(word.find('G'))
print(word.rfind('G'))

print(word.split())
word2 = 'Good/manufacturing/Practice/Good'
print(word2.split('/'))

word3 = ' hello world '
print(len(word3), len(word3.strip()), word3.strip())
print(len(word3.rstrip()), word3.rstrip())

print(word.startswith('G'))
print(word.endswith('G'))

for val in word:
    print(val, word.count(val))