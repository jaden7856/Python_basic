def add(num1, num2 =20):
    return num1 + num2

print("입력하고 싶은 숫자를 입력하세요")
val = int(input())
print(type(val))

result = add(val)
print(result)