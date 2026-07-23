dict1 = {'mom': '3802342343',
         'qwerty': '12312312'}

print(type(dict1))
print(dict1)

student = {'name': "Max",
           'age': 20,
           'city': "Dnipro"}

print(f"Student name: {student['name']}")
# change elem
if 'age' in student:
    student['age'] = 21
print(student)

# add new elem
student['phone'] = '38923234323'
print(student)

# email , curs , avg_mark

print(dict(zip([1, 2, 3], [11, 22, 33])))
print(dict(**student))

print(len(student))

# student.pop('phone')
# print(student.popitem())
# print(student.popitem())
student.update(dict1)
print(student.values())
print(student.keys())
print(student.items())
print(student)

for key, value in student.items():
    print(key, value)

print(student['name'])
print(student.get('name2'))

# case 1

users = [
    {'name': 'Bill', 'age': 30, 'login': "qwerr"},
    {'name': 'Mark', 'age': 28, 'login': "123asd"},
    {'name': 'Den', 'age': 39, 'login': "fsdfd"},
    {'name': 'Ilon', 'age': 45, 'login': "1111"}
]
#
# keyName = input("Input info type - ")
# keyValue = input("Input info value - ")
# keyValue = keyValue if keyName != 'age' else int(keyValue)
#
# isElementFound = False
#
# for user in users:
#     if user.get(keyName) == keyValue:
#         print("Element is found !")
#         for key, val in user.items():
#             print(f"{key} : {val}")
#         isElementFound = True
#         break
#
# if not isElementFound:
#     print("Element is not found !")

# case 2

filmDict = {
    'originalTitle': 'Python',
    'creator': 'Gvido',
    'rate': 9,
    'description': "Film about python",
    'year': [1991, 1992]
}

for key, value in filmDict.items():
    print(f"{key} {value}")

sortedFilm = sorted(filmDict.items(), key=lambda x: x[0])
print(sortedFilm)
for elem in sortedFilm:
    print(elem)

keyList = list(filmDict.keys())
print(keyList)

sortedKeys = sorted(keyList)
print(sortedKeys)

for key in sortedKeys:
    print(key, filmDict[key])

users = [
    {'name': 'Bill', 'age': 30, 'login': "qwerr"},
    {'name': 'Mark', 'age': 28, 'login': "123asd"},
    {'name': 'Den', 'age': 39, 'login': "fsdfd"},
    {'name': 'Ilon', 'age': 45, 'login': "1111"}
]

sortedUsersByName = sorted(users, key=lambda x: x['age'])
print(sortedUsersByName)

users30 = list(filter(lambda user: user['age'] > 30, users))

print(users30)
