# i = 1
# while i <= 5:
#     print(f"i = {i}")
#     i += 1
#
#
# i = 10
#
# while i > 0:
#     print(f"i = {i}")
#     i -= 1

# while True:
#     num = int(input("Enter number = "))
#     if num == 0:
#         print("Stop while")
#         break
#     if num == 100:
#         print("Stop while")
#         break
#     print(num)


# while True:
#     print(f"------Menu-----\n1.Show number\n2.Show word\n3.Exit")
#     choice = input("Enter your choice (1,2,3) = ")
#     if choice == '1':
#         print("123")
#     elif choice == '3':
#         break
#     else:
#         print("Error input!")

# continue - пропуск поточної ітерації


# while True:
#     num = int(input("Enter number = "))
#     if num % 2:
#         print("next iteration")
#         continue
#     if num == 0:
#         print("Stop while")
#         break
#     if num == 100:
#         print("Stop while")
#         break
#     print(num ** 2)

# while True:
#     password = input("Enter password - ")
#     if password == '':
#         print("Cant be empty!")
#         continue
#     if password == 'admin':
#         print("OK")
#         break
#     print("Error password !")

#  for in

for i in 1, 2, 3, 4, 5:
    print(f"i = {i}")

# range()
print(list(range(10)))
print(list(range(20)))
print(list(range(1000)))
print(list(range(1, 11)))
print(list(range(10, 1, -1)))

for num in range(20):
    if num % 2:
        continue
    print(num, end=" ")
    if num == 10:
        break
print()

for s in "python":
    print(s)

num = 2
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")




