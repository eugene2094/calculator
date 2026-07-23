print("Hello !")
print("Hello !")
print("Hello !")
print("Hello !")
print("Hello !")


def welcome():
    print("Hello from func!")


welcome()

welcome()

welcome()

print("qwe", 123, [1, 2, 3])

print(type(range(1, 10, 2)))

print(len([1, 2, 3]))

print(abs(-20))

print(round(5.368, 1))

# min()  max() sum()

print(sum([1, 2, 3]))
print(pow(2, 3))

print(divmod(17, 5))

hours, minutes = divmod(130, 60)
print(f"Hours: {hours}, minutes: {minutes}")

import random

print(random.choice(['1', '2', '3']))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

help(random)


# створення функції

def hello():
    print("Hello from func!")


def print_line():
    print("-" * 50)


# виклик функції
hello()
print_line()
hello()
print_line()
hello()


def greet(name):
    print("Hello,", name)


greet("Bob")
greet("Max")


def show_user_info(name, age):
    print(name)
    print(age * 7)


age = 12

show_user_info("max", age)


def add(num1, num2):
    print("before return")
    return num1 + num2


def get_info():
    return 'max', 20, "12312312"


result = add(2, 2) * 2
print(result)

result = get_info()
print(result)


def menu(chooce):
    if chooce == 1:
        return "Your choice 1"
    elif chooce == 2:
        return "Your choice 2"


print(menu(2))
