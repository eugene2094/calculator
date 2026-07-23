num1 = 10
num2 = 11
num3 = 10

# list - набір даних
marks = [10, 9, 11, 12, 6]
print(type(marks))
print(marks)
names = ['Ilon', 'Bill', 'Bob', 'Djon']
print(names)

data = [12, 0.5, 'text', True, 12, 12]
print(data)

nums = list((1, 2, 3))
print(nums)

print(names[0])
print(names[-1])
print(names[0:2])
print(names[2:])
print(names[0:3:2])
print(names[4:0:-1])

print(len(names))

names[0] = 'Kate'
print(names)

for s in "python":
    print(s)

for elem in marks:
    print(f"elem: {elem}", end=" | ")
print()
print(marks)

sum_marks = 0
for mark in marks:
    sum_marks += mark

print(f"avg mark: {sum_marks / len(marks)}")

min_mark = marks[0]
for mark in marks[1:]:
    if mark < min_mark:
        min_mark = mark

print(f"Min mark: {min_mark}")

print(sum(marks))
print(min(marks))
print(max(marks))

product_list = ['banana', 'milk']
print(product_list)
product_list.append('bread')
print(f"After add: {product_list}")
product_list.insert(-1, 'meat')
print(f"After insert: {product_list}")

product_list.pop(0)
print(f"After del: {product_list}")
if 'bread' in product_list:
    product_list.remove('bread')
print(f"After del: {product_list}")

print(product_list.count('meat'))

