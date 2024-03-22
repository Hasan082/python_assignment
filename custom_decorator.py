def custom_decorator(func):
    def inner(a, b):
        if b != 0:
            return func(a, b)
        else:
            return "Can not divided by Zero"
    return inner

# Custom decorator function
@custom_decorator
def division(a, b):
    c = a / b
    return c

print(division(10, 0))