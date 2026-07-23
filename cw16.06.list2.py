numbers = [1, 2, 3, 4, 5]
print(numbers)

squares = []
for i in range(1, 11):
    if i % 2:
        squares.append(i ** 2)
print(squares)

# [вираз for elem in послідовність]

squares = [x ** 2 for x in range(1, 11)]
print(squares)

list2 = [i * 3 for i in "abc"]
print(list2)

even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)

prices = [100, 200, 300]
news_prices = [price * 0.9 for price in prices]
print(prices)
print(news_prices)

matrix = [[0 for j in range(3)] for i in range(3)]
print(matrix)

import random

rand_nums = [random.randint(-100, 100) for i in range(1000)]
print(rand_nums)

user_str = '2,2,224,5'
list_nums = [int(x) for x in user_str.split(',')]
print(list_nums)

list_nums.extend([1, 2, 3])
print(list_nums)

list_nums.copy()

new_list = list_nums.copy()
print(new_list)
new_list[0] = -1
print(list_nums)

new_list.sort(reverse=True)
print(new_list)

words = ['athg', 'bc', 'a']
words.sort(key=len)
print(words)

del new_list[0]
print(new_list)

grades = [
    [10, 12, 11],
    [9, 10, 12],
    [11, 8, 10]
]

grades[1][0] = 11

for row in grades:
    for col in row:
        print(col, end="  ")
    print()

matrix = [[0 for j in range(4)] for i in range(4)]

for row in matrix:
    for col in row:
        print(col, end="  ")
    print()

maximum = grades[0][0]

for row in grades:
    for elem in row:
        if elem < maximum:
            maximum = elem


print(maximum)
