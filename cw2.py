print(100)
print(7.5)
print("hello\nworld", 123, 'test1', sep=' --  ')

print(1, end=' - ')
print(2)

# змінна - комірка памяті для збереження данних

name = "Boris"
number = 1
user_login = "qwerty"
num1 = 1

a = 1
b = 3

print('hello', name)

# 2) Типи змінних   int, float, str, bool

# int  100, -2 ,0
number2 = 100
print(type(number2))

# float  3.5 , 5.0,  -6.7
num_pi = 3.14
print(type(num_pi))

# str рядок "text"

password = "'qwerty's "
login = '"qwerty"'
print(type(password))
print(type(login))
print(login)

mega_text = """
# float  3.5 , 5.0,  -6.7
num_pi = 3.14
print(type(num_pi))

# str рядок "text"

password = "'qwerty's "
login = '"qwerty"'
print(type(password))
print(type(login))
print(login)
"""
print(mega_text)

# bool  True False

check = True
print(type(check))

#  input()

name = input("Enter your name -> ")
print("hi", name)

salary = int(input(f"Enter your salary {name}"))
print('Salary:', salary, '$')
print(type(salary))
print("END")

count = 100
print(str(count))

print(f"Count: {count}")


NUMBER = 1

print(NUMBER)
NUMBER += 1

print(NUMBER)

