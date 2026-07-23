# декоратори

def hello():
    print("Hello")


n = 100
a = hello

a()


def execute(func):
    func()


execute(hello)


# 1 decorator

def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


newHello = decorator(hello)
newHello()


@decorator
def hello2():
    print("hi")


hello2()


def decorator_v2(func):
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")

    return wrapper


@decorator_v2
def add(a, b, c):
    print(a + b + c)


add(2, 2, 3)


def decorator_v3(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print(result)
        print("End")
        return result

    return wrapper


@decorator_v3
def mul(a, b, c):
    return a * b * c


mul(2, 2, c=2)

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result

    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@timer
@logger
def sleep():
    time.sleep(1)


sleep()


def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return func(*args, **kwargs)

    return wrapper


@counter
def show():
    print("test work")


for i in range(5):
    show()


# decorator with args
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hello3():
    print("Hey")


hello3()
