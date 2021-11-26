# decorators helps to extend functions without changing them

def decorator_function(math_func):
    def num_tuple(tuple_list):
        return [math_func(num[0], num[1]) for num in tuple_list]
    return num_tuple


@decorator_function
def math_sum(a, b):
    return a+b


print(math_sum([(4,6), (5,7), (5,10)]))
