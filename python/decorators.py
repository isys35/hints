import functools


def decorator1(func):
    def wrapper():
        print('Привет')
        func()
        print("Пока")

    return wrapper


def hello_function():
    print('Я функция')


func = decorator1(hello_function)
func()


@decorator1
def hello_function():
    print('Я функция')


hello_function()


def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Привет {args[0]}')
        func(*args, **kwargs)
        print(f'Пока, {args[0]}')

    return wrapper


@decorator2
def hello_function2(name):
    print(f'Функция для {name}')


hello_function2('Дмитрий')

print(hello_function2.__name__)
help(hello_function2)


def repeat_hello(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, *kwargs)

        return wrapper

    return decorator


@repeat_hello(5)
def hello_function2(name):
    print(f'Функция для {name}')


hello_function2('Димоооон')


def counter(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            nonlocal count
            count += 1
            print(count)
        return wrapper
    return decorator


@counter(count=0)
def hello_function2(name):
    print(f'Функция для {name}')


hello_function2('Дн')
hello_function2('Д')
hello_function2('kkkkk')
hello_function2('vgh')
hello_function2('он')
