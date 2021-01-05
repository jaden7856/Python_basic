num_list = [10, 20, 40, 50, 60]
num_list2 = [1, 2, 3, 4, 5]

# 리스트 메모리 저장 방식
print((num_list, num_list2))
num_list2 = num_list
print((num_list, num_list2))
num_list.sort()
print((num_list, num_list2))
num_list2 = [1, 2, 3, 4, 5]
num_list.sort()
print((num_list, num_list2))


print(type(num_list), num_list)
print(num_list[0], num_list[0:3], num_list[3:])

for idx, num in enumerate(num_list):
    print(idx, num)


str_list = ['pyhon', 'java', 'kotlin', 'C++', 'Scalar']
print(type(str_list), str_list)
# 값 변경
str_list[1] = 'java script'
print(str_list[1], str_list[2:4])
# 값 추가
str_list.append('Cobol')
str_list.insert(1, 'type script')
print(str_list)
# 값 삭제
str_list.remove('Cobol')
print(str_list)


for idx, val in enumerate(str_list):
    print(idx, val)

mix_list = [100, 3.14, True, '파이썬']
for mix in mix_list:
    print(type(mix), mix)

my_list = list('Python') # str -> list
print(my_list, type(my_list))
my_list2 = 'Hello, Python'.split(',') # str -> list
print(my_list2)

# packing and unpacking
# packing
my_list3 = ['aa', 'bb']

# index checking
print(my_list3.index('bb'))
print(my_list3.count('bb'))

# unpacking
str1, str2 = ['cc', 'dd']
print(str1, type(str1))
print(str2, type(str2))