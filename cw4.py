# >  <   <=  >=   ==  !=
#  and or not

print(2 == 2)
print(1 < 10)
print(1 > 10)
num = 10
print(num != 1)

print(num > 0 and num == 12)
print(num > 0 or num == 12)
print(not True)
print(not False)

print(bool(not 1))
print(bool(-2))
print(bool(0))

print('p' not in 'python')

print("qwerty" == '123')

car_speed = 51

if car_speed > 50:
    # дія, яка спрацює за правдивої умови
    print("Ha ha ha Ви отримали штраф !!!! ")

if car_speed > 50 and car_speed < 150:
    print("Speed between 50 - 150 !")

year = 2005

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"Year {year} is leap!")

if car_speed < 50:
    print("Speed is ok")
else:
    print("Error speed!")

age = 5

if age < 6:
    print("child")
# if age >= 6 and age < 18:
elif 6 <= age < 18:
    print("Schoolar")
elif 18 <= age < 22:
    print("student")
else:
    print("Error")

number = int(input("Enter number - "))
if number == 1:
    print("You have  chosen answer A")
else:
    if number == 2:
        print("You have  chosen answer B")
    else:
        if number == 3:
            print("You have  chosen answer C")
        else:
            if number == 4:
                print("You have  chosen answer D")
            else:
                print("No such answer!")

number = int(input("Enter number - "))
if number == 1:
    print("You have  chosen answer A")
elif number == 2:
    print("You have  chosen answer B")
elif number == 3:
    print("You have  chosen answer B")

login = input("Enter login - ")
password = input("Enter password - ")

if login == 'admin':
    print("Login is true!")
    if password == 'admin':
        print("password is true!")
    else:
        print("Error password!")
else:
    print("Error login!")
