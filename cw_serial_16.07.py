import pickle, json

student = {
    'name': 'Max',
    'age': 23,
    'grades': [10, 11, 10]
}
# виконали серіалізацію зі збереженням у файл
with open('students.pkl', 'wb') as file:
    pickle.dump(student, file)

with open('students.pkl', 'rb') as file:
    student = pickle.load(file)
print(student)

with open('student.json', 'w') as file:
    json.dump(student, file, indent=4)

with open("student.json", 'r') as file:
    st = json.load(file)

print(st)

import csv

with open('student.csv', 'w', newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Phone'])
    writer.writerow(['Max', '34', '332314134'])
    writer.writerow(['Ben', '12', '434343434'])

with open("student.csv", encoding='utf-8') as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row)

with open('student.csv') as file:
    reader = csv.DictReader(file)
    for st in reader:
        print(st)

with open('employee.csv', 'w',newline="") as file:
    field_names = ['name', 'salary']
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'name': 'Max', 'salary': 1000})

