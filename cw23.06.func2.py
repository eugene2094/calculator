# def add(a, b):
#     return a + b
#
#
# res = add(2, 3)
# print(res)
#
#
# def greet(name='guest'):
#     print(f"Hello {name}")
#
#
# greet("Max")
#
#
# def power(number, degree=2):
#     return number ** degree
#
#
# print(power(2))
# print(power(2, 3))
#
# print(power(degree=4,
#             number=3
#             ))
#
#
# def total(*args):
#     print(args)
#     return sum(args)
#
#
# total(1, 2, 3)
# print(total(1, 2))
#
# nums = [1, 2, 3]
#
# print(total(*nums))

# namespace global
global_num = 100

# from random import randint
import random


def choice():
    pass


def test():
    # namespace local
    global global_num
    x = 10
    print(x)
    global_num = 500
    print(f"glob num: {global_num}")


# print(x)
test()

gx = 2
print(gx)
print(f"glob num: {global_num}")


def outer():
    value = 0

    def inner():
        nonlocal value
        print("Inner func working")
        value = 1
        print(value)

    inner()
    print(value)


outer()


def countDown(n):
    if n == 0:
        return
    print(n)
    countDown(n - 1)


countDown(5)


def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num - 1)  # 5 * 4 * 3 * 2 * 1


print(factorial(5))
