# # 1
#
# number = int(input("Enter number - "))
# count = 0
#
# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i)
#         count += 1
#
# print(f"Count : {count}")
#
# # 2
#
# number2 = int(input("Enter number - "))
# sum_divisors = 0
#
# for i in range(1, number2):
#     if number2 % i == 0:
#         sum_divisors += i
#
# if sum_divisors == number2:
#     print("Досконали")
# else:
#     print("Не досконале !")
#
# a = number // 100
# b = number // 10 % 10
# c = number % 10
#
# print(f"a= {a}, b= {b}, c = {c}")

import random

while True:

    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        print()
        print("--- GAME Rock, Scissors, Paper ---")
        print("r - Rock\ns - Scissors\np - Paper\ne - exit")
        print()
        user = input("Enter your choice - ")
        if user == 'e':
            print("Game over")
            break
        if user not in 'rpse':
            print("Error input, try again!")
            continue

        comp = random.choice('rps')
        rounds += 1
        print(f"Computer choice - {comp}")

        if comp == user:
            print("Tie!")
        elif user == 'r' and comp == 's' or user == 's' and comp == 'p' or user == 'p' and comp == 'r':
            print("User win !")
            player_score += 1
        else:
            print("Comp win!")
            computer_score += 1

        print(f"Your score: {player_score}")
        print(f"Comp score {computer_score}")
        print(f"Round number {rounds}")

        if player_score == 3:
            print("User win the game !")
            break
        elif computer_score == 3:
            print("Comp win the game !")
            break

    choice = input("Do you want to start new game ? (y/n)")
    if choice == 'y':
        continue
    else:
        break
