def square(x):
    return x * x


result = square(2)
print(result)

numbers = [1, 2, 3, 4, 5]
result = []

for num in numbers:
    result.append(num ** 2)

print(result)

result = list(map(lambda x: x ** 2, numbers))
print(result)


def greet(name):
    return f"Hello, {name}"


print(greet("max"))

message_func = greet
print(message_func("Anna"))


def apply_operation(a, b, operation):
    return operation(a, b)


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


print(apply_operation(2, 3, multiply))
print(apply_operation(4, 5, add))


def nameUpper(name):
    return 'user' + name.upper()


def nameLower(name):
    return 'user' + name.lower()


def makeLog(userName, maker):
    return maker(userName)


print(f"New login: {makeLog('max', nameLower)}")
print(f"New login: {makeLog('max', nameUpper)}")

# lambda

square = lambda x: x ** 2
print(square(3))

add = lambda a, b: a + b
print(add(3, 5))

is_even = lambda x: x % 2 == 0
print(is_even(10))
print(is_even(3))

maximum = lambda a, b: a if a > b else b

print(maximum(8, 3))

students = [['Bob', 70], ['Jane', 60], ['Nick', 88]]
print(students)

sortedSts = sorted(students, key=lambda x: x[0])
print(sortedSts)

studBirthYear = [2000, 1997, 2003, 1996]

studYears = []

for year in studBirthYear:
    studYears.append(2026 - year)

print(studYears)

studAges = list(map(lambda year: 2026 - year, studBirthYear))
print(studAges)

userLogs = ['Admin', 'STUDENT', 'QEWgskd', 'User']
print(userLogs)

userLogsLower = list(map(str.lower, userLogs))
print(userLogsLower)

myValues = ['2', '4.6', '7.9']
myNumbers = list(map(float, myValues))
print(myNumbers)


def modifyPizzaTypes(pizzaType):
    return pizzaType + " Pizza"


pizzaTypes = ['Meat', '4Cheese', 'Margorita']
print(pizzaTypes)
pizzaNames = list(map(modifyPizzaTypes, pizzaTypes))
print(pizzaNames)

# filter

prices = [100, 8, 56, 34, 120, 230]
expensive = list(filter(lambda x: x >= 100, prices))

print(expensive)


def checkLog(user):
    # if user.lower().find('user') != -1:
    #     return True
    # else:
    #     return False
    return user.lower().find('user') != -1


# zip

userLogs = ['123rqwer', 'asdqwe', '5345dgd']
userPass = ['111', '3232', '4343','312']

for log, passw in zip(userLogs, userPass):
    print(f"login: {log}, pass: {passw}")

print(list(zip(userLogs, userPass)))

