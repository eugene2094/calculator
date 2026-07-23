students = ['Anna', 'Bill', 'Max']

print(students)

# name = input("Enter name - ")
# students.append(name)
print(students)

file_name = 'students.txt'
# file = open(file_name, 'w', encoding='utf-8')
# for st in students:
#     file.write(st + '\n')
# file.close()

student = {
    'name': "Max",
    'age': 15,
    'grade': 11
}

# file = open(file_name, 'w', encoding='utf-8')
# for key, value in student.items():
#     file.write(f"{key} : {value}\n")
#
# file.close()

file = open('students.txt', 'r', encoding='utf-8')
# data = file.read(5)
# data2 = file.read(10)
# print(data2)
data = file.readline()
allLines = file.readlines()
print(data)
print(allLines)
file.close()

# режими роботи з файлом  w, r, a, b, x

file = open(file_name, 'a', encoding="utf-8")
file.seek(0, 0)
print(file.tell())
file.write('Ben\n')
file.close()
