# Оператори + -  * /  //  **  %

print(2 + 2)
print(-4)

num1 = 10
num2 = 2

result = num1 + num2
print(f"result = {result}")
result = num1 - num2
print(f"result = {result}")
result = num1 * num2
print(f"result = {result}")
result = num1 / num2
print(f"result = {result}")

result = num1 // 3
print(f"result = {result}")

result = num1 ** 3
print(f"result = {result}")

result = 7 % 3
print(f"result = {result + 2}")

# 1) **
# 2) *, /, //, %
# 3) +, -
# 4) =


print((2 + 2) * 3)

print(15 % 4)
print(20 // 6)
print((10 - 2) * 3)
print(5 ** 2)

text = "python"

text2 = " cool"
# + для рядків - конкатенація

print(text + text2)

text = "qwerty "

print(text * 2)
print("_" * 30)

# print(text / 2)
# print(10 / 0)

# Завдання 1
# Користувач вводить з клавіатури два числа. Розрахуйте суму чисел, різницю чисел, добуток чисел. Результати обчислень виведіть на екран.

# number1 = int(input("Enter first number - "))
# number2 = int(input("Enter second number - "))
#
# print(f"{number1} + {number2} = {number1 + number2}")
# print(f"{number1} - {number2} = {number1 - number2}")
# print(f"{number1} * {number2} = {number1 * number2}")

# Завдання 2
# Користувач вводить з клавіатури два числа. Перше число — це значення, друге число — відсоток, який необхідно підрахувати.
# Наприклад, ми ввели з клавіатури 50 та 10. Виведіть на екран 10% від 50. Результат: 5.

# number1 = int(input("Enter first number - "))
# number2 = int(input("Enter second number - "))
# print(f"{number2}% for {number1} = {(number1 * number2) / 100}")
#


# Користувач вводить з клавіатури тризначне число. Наприклад, 891. Покажіть на різних рядках значення першого, другого та третього розряду.
# Також виведіть на окремий рядок суму цих трьох чисел.

num = int(input("enter num - "))

n1 = num // 100
print(n1)

n2 = (num // 10) % 10
print(n2)

n3 = num % 10
print(n3)

