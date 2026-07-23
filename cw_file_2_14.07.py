# with
opened = False
try:
    file = open('notes.txt')
    opened = True
    number = 10 / 0
    text = file.read()
    print(text)
    file.close()
    print("closed")

except Exception as ex:
    print(ex)
finally:
    if opened:
        print("File closed")
        file.close()

with open('notes.txt', 'r') as file:
    text = file.read()
    print(file.closed)

print(text)
print(file.closed)
count = 0
with open('notes.txt', 'r') as file:
    longest = ''
    for line in file:
        count += 1
        word = line.strip()
        if len(word) > len(longest):
            longest = line

print(count)
print(longest)

files = ['file1.txt', 'file2.txt', 'file3.txt']

with open('merged.txt', 'w', encoding='utf-8') as merged:
    for file_name in files:
        merged.write(f"====== {file_name} =======\n")
        with open(file_name, 'r') as file:
            merged.write(file.read())
        merged.write("\n\n")

with open('file1.txt', 'r', encoding='utf-8') as f1:
    lines1 = f1.readlines()

with open('file2.txt', 'r', encoding='utf-8') as f2:
    lines2 = f2.readlines()

max_length = max(len(lines1), len(lines2))

with open('merged_alternate.txt', 'w', encoding='utf-8') as result:
    for i in range(max_length):
        if i < len(lines1):
            result.write(lines1[i])
        if i < len(lines2):
            result.write(lines2[i])

print("чергуючи рядки дані записано у результат")

# 5
file_name = 'library.txt'


def add_book():
    title = input("Enter name - ")
    auther = input("Enter auther name - ")

    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"{title} : {auther}\n")

    print("Book added!")


def show_books():
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            books = file.readlines()
        if not books:
            print("Library is empty!")
            return
        print("Books list:\n")
        # for book in books:
        #     print(book)
        for i, book in enumerate(books, start=1):
            title, auther = book.strip().split(":")
            print(f"{i}. {title} - {auther}")
    except FileNotFoundError:
        print("File was not created !")


def search_book():
    keyword = input("Enter name of the book or auther - ").lower()
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            found = False
            for book in file:
                title, auther = book.strip().split(":")
                if keyword in title.lower() or keyword in auther.lower():
                    print(f"{title} - {auther}")
                    found = True
            if not found:
                print("This book not found!")

    except FileNotFoundError:
        print("File not found !")


def main():
    while True:
        print("\nMenu")
        print('1. - Add book')
        print('2. - Show book')
        print('3. - Search book')
        print('4. - Delete book')
        print('5. - Exit')
        choice = input("Enter your choice - ")

        match choice:
            case '1':
                add_book()
            case '2':
                show_books()
            case '3':
                search_book()
            case '5':
                break
            case _:
                print("Error input")
main()


