'''
 키워드 파라미터
'''


def connect(server, port):
    url = f'http://{server}:{port}'
    return url


print(connect('localhost', '8080'))
print(connect(port='8080', server='localhost'))

'''
 Argument Default Value
'''


def times(a=10, b=20):
    return a * b


x = times()
y = times(5)
print(x, y)

'''
 가변(파라미터의 갯수가 정해지지 않음) 파라미터
'''


# tuple 타입
def kwargs_test(a, b, *c):
    return a + b + sum(c)


print(kwargs_test(10, 20))
print(kwargs_test(2, 3, 4, 5, 6, 7))


# dict 타입
def kwargs_dict(a, b, **c):
    print(type(c))
    for k, v in c.items():
        print(k, v)

#kwargs_dict(10, 20, 30)


# return 값에 tuple 로 반환
def swap(a, b):
    return b, a

r, s = swap(20, 8)
print(r, s)
