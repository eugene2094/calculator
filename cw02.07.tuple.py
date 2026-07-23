numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

for i in range(len(numbers)):
    numbers[i] += 10
    print(numbers[i])

# tuple  кортеж

NUMBER_PI = 3.14
print(NUMBER_PI)
NUMBER_PI = "qwerty"

# creating tuple

years = (2000, 2005, 1998, 2001)
print(years)
print(type(years))
# TypeError: 'tuple' object does not support item assignment
# years[0] = 1999

empty = ()
print(type(empty))

nums = ("1",)
print(type(nums))

numbers = tuple(numbers)
print(type(numbers))

# Доступ до елементів
colors = ('red', 'green', 'blue')

print(colors[1])
print(colors[-1])
print(colors[:2])
print(colors[::-1])

# Основні методи

# len() min() max() sum()

print(colors.count('black'))
if 'green2' in colors:
    print(colors.index('green2'))


def showNums(*nums):
    print(type(nums))
    print(nums)


showNums(1, 2, 3, 4, 5)

person = ('Max', 20)

name, age = person
print(name)
print(age)

# a, b, c = (1, 2, 3)
a = 1
b = 2
a, b = b, a
print(a, b)

students = (
    ('Ivan', 23),
    ('Max', 19),
    ("Oleg", 21)
)
print(students[1][1])

# set
emails = [
    'ivan@gmail.com',
    'ivan@gmail.com',
    'max@gmail.com',
    'Bill@gmail.com',
    'Kate@gmail.com'
]

unique = set(emails)
print(unique)

numbers = {1, 2, 3, 4, 4, 4, 5}
print(numbers)

# set()
nums = [2, 2, 3, 3, 4, 4]
print(set(nums))

s = set()
print(type(s))

# Methods
numbers.add(123)
print(numbers)
numbers.pop()
print(numbers)

users = {'qwerty', 'admin', 'asd'}
# print(users.pop())
# users.remove('qwerty')
# users.discard('asd')
# users.discard('asd')
# users.remove('asd')
print(users)

iphoneSet1 = {'iphone11', 'iphone12', 'iphone13'}
iphoneSet2 = {'iphone13', 'iphone12', 'iphone15', 'iphone17'}

# diference
print(iphoneSet1.difference(iphoneSet2))
print(iphoneSet2.difference(iphoneSet1))
print(iphoneSet1 - iphoneSet2)

# intersection

print(iphoneSet1.intersection(iphoneSet2))
print(iphoneSet2 & iphoneSet1)

# union
print(iphoneSet1.union(iphoneSet2))
print(iphoneSet2 | iphoneSet1)

# frozenset()

frozenA = frozenset(iphoneSet1)
print(frozenA)


