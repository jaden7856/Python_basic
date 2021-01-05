# 클래스 선언
# class MyClass extends Object {}, class MyClass { } - Java
# class MyClass(object): , class MyClass: - Python

# class MyClass(object):
class Myclass:
    # constructor 생성자 선언
    def __init__(self):
        # attribute(속성) 초기화
        self.num = 100
        # private 속성 = '__'
        self.__name = 'Jaden'

    # method(행위) 선언
    def read_number(self):
       return self.num + 100

    def __str__(self):
        return f'MyClass의 속성 : {str(self.num)}, 이름 : {self.__name}'

    # getter method
    @property
    def name(self):
        return self.__name

    # setter method
    @name.setter
    def name(self, new_name):
        if len(new_name) == 3:
            self.__name = new_name
        else:
            print('새로운 이름의 길이는 3이여야 합니다.')


# 객체를 생성
if __name__ == '__main__':
    myobj = Myclass()
    print(myobj)
    print(myobj.read_number())

    # getter method 호출
    print(myobj.name)
    # setter method 호출
    myobj.name = '홍길동'
    print(myobj.name)
