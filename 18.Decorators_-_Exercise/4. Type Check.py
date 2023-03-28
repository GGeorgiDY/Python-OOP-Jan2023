def type_check(expected_type):
    def decorator(func):
        def wrapper(number):
            if type(number) == expected_type:
                return func(number)
            else:
                return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
