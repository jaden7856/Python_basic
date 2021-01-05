'''
 섭씨를 화씨로 변환
'''

def TempConvert(Cel):
    result = ((9/5) * float(Cel)) + 32
    return round(result, 2)

def sayHello(msg):
    return f'Hello {msg}!'


