# for i in range(1, 11):
#     print(i)
#
# while True:
#     command = input("Enter exit: ")
#
#     if command == 'exit':
#         break
#
# while True:
#     print("------ Converter usd -----------")
#     print("1 - usd to uah")
#     print("2 - euro to uah")
#     choice = input("Enter num - ")
#
#     if choice == '1':
#         money = float(input("Enter usd - "))
#         result = money * 44
#         print(f"Result {result} uah")
#     elif choice == '2':
#         money = float(input("Enter euro - "))
#         result = money * 52
#         print(f"Result {result} uah")
#     elif choice == '0':
#         break
#     else:
#         print("Error input!")

# max_num = 0
#
# while True:
#     number = int(input("Enter number - "))
#     if number == 0:
#         break
#     if number > max_num:
#         max_num = number
#         print("Update max number: ", max_num)
#
# print("Max number: ", max_num)
#


for i in range(3):
    print("Hello")

for row in range(3):
    # print("Outer loop")
    for col in range(3):
        print("*", end="  ")

    print()

for i in range(1, 6):
    for j in range(i):
        print("*", end="  ")

    print()

height = 5

for row in range(height):
    for space in range(height - row - 1):
        print(" ", end="")
    for star in range(2 * row + 1):
        print("*", end="")

    print()

# гра Вгадай число
import random

random_number = random.randint(1, 10)
print(random_number)

tries = 0

while True:
    user_number = int(input("Enter number 1-10 - "))
    # 1) обробити вихід числа  за межі
    if user_number == 0:
        print("Game over !")
        break
    tries += 1
    if user_number == random_number:
        print("Winnnnn!")
        print(f"Count tries {tries}")
        break
    elif user_number < random_number:
        print("Try bigger!")
    else:
        print("Try lower!")
# 2) можливість зіграти ще раз 
