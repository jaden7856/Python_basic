# 일반적인 for + append
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
print(result)


# List Comprehensions
result = [i for i in range(10) if i % 2 == 0]
print(result)

my_str1 = 'Hello'
my_str2 = 'World'
result = [i+j for i in my_str1 for j in my_str2 if not (i == j)]
print(result)

words = "Trump demands Georgia officials find votes to tilt election".split()
my_list = [[w.upper(), w.lower(), len(w)] for w in words]
print(my_list)
for word in my_list:
    print(word)

# enumerate 함수 - for loop를 dict에 저장
for idx, word in enumerate(words):
    print(idx, word)

word_dict = {idx : w for idx, w in enumerate(words, 1)}
print(word_dict)


# zip 함수
list_zip1 = [1, 2, 3]
list_zip2 = [10, 20, 30]
list_zip3 = [100, 200, 300]

for val in zip(list_zip1, list_zip2, list_zip3):
    print(sum(val))

result = [sum(val) for val in zip(list_zip1, list_zip2, list_zip3)]
print(result)

result_dict = {idx : sum(val) for idx, val in enumerate(zip(list_zip1, list_zip2, list_zip3))}
print(result_dict)

a, b, c = zip(list_zip1, list_zip2, list_zip3)
print(type(a), a)
print(b)
print(c)