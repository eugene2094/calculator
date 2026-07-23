print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")

# ітерація - одне виконня циклу

# while - цикл з умовою

i = 1
while i <= 5:
    # print(f"i={i}")
    print("Hello")
    i += 1  # i = i + 1

# 2
n1 = 1
while n1 < 11:
    print(n1)
    n1 += 1

# 3
print("----------------3-------------------")
n1 = 10
while n1 >= 1:
    print(n1)
    n1 -= 1

# 4
print("---------------4-----------------")
n1 = 1
while n1 < 11:
    if not n1 % 2:
        print(n1)
    n1 += 1

# while True:
#     word = input("Enter word - ")
#
#     if word == 'stop':
#         break  # stop while
#     print(f"Your word {word}")

# while True:
#     password = input("Enter password ")
#     if password == 'admin':
#         break
#     print("Error password")
# print("Password is ok")

num = 1
sum = 0
while num != 0:
    try:
        num = int(input("Enter num - "))
        print(num)
        sum += num
    except ValueError:
        print("Error value")
print(f"Result: {sum}")

while True:
    print("-- Menu --")
    print(" 1 Balance")
    print(" 2 Exit")
    choice = int(input("Press btn - "))
    if choice == 1:
        print("Balance 1000")
    elif choice == 2:
        print("End work")
        break

