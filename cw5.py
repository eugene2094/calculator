# Винятки

# print(10/0)

# print("qwe" + 12)

# try:
#     amount = int(input("Enter amount - "))
#     items_type = input("Enter type - ")
#
#     parts_number = int(input("Enter the number of parts - "))
#     parts_amount = amount / parts_number
#     print(f"We got {amount} {items_type} ")
#     print(f"Parts amount of product {parts_amount}")
# except ValueError:
#     print("Amount should be an integer!")
# except ZeroDivisionError:
#     print("Number parts cant be zero !")
# except Exception as ex:
#     print("We have error - ", ex)
# finally:
#     print("The program has finished!")
#

try:
    age = int(input('Enter age - '))
    if age < 0:
        raise ValueError

except Exception:
    print("Age must be > 0!")
else:
    print('Your age is ok')
