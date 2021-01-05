'''
 Stack과 Queue 를 List 로 작성한다.
'''

stack_list = [1, 2, 3]
stack_list.append(5)
stack_list.extend([10, 20])
print(stack_list)

# LIFO
stack_list.pop()
print(stack_list)
stack_list.pop()
print(stack_list)

# FIFO
queue_list = [10, 20, 30]
queue_list.pop(0)
print(queue_list)

# tuple
my_tuple = tuple([10, 30, 40])
my_tuple2 = (20, 30, 40)
print(type(my_tuple), type(my_tuple2))
print(my_tuple[2], my_tuple2[0:2], my_tuple * 2)

my_int = (10)
my_tuple3 = (10, )
print(type(my_int), type(my_tuple3))

# set 중복을 허용하지 않음
my_set = set([1, 2, 3, 1, 2, 3])
print((type(my_set), my_set))
my_set.add(1)