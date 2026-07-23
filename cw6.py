# Завдання 1 — “Сейф”
# Умова
#
# Є секретний код. Користувач вводить код.
# Якщо код правильний — сейф відкрито.
# Якщо ні — помилка.
# Якщо ввели текст — обробити виняток.

# secret_code = 1111
# try:
#     user_code = int(input("Enter code - "))
#     if user_code == secret_code:
#         print("Open!")
#     else:
#         print("Error code!")
# except ValueError:
#     print("Error: code must be integer!")
# except Exception as ex:
#     print(ex)

#
# Завдання 2 — “Квитки в кіно”
# Умова
#
# Ціна квитка — 150 грн.
# Користувач вводить вік і кількість квитків.
#
# Правила:
#
# до 12 років — знижка 50%;
# від 60 років — знижка 30%;
# інші — без знижки.


# Варіант 1 — “Каса магазину”
# Умова
#
# Є меню товарів:
#
# молоко — 50 грн;
# хліб — 30 грн;
# сік — 70 грн.
#
# Користувач обирає товар, кількість і вводить суму оплати.
# Програма рахує чек і решту.
#

print("---------------- Menu ---------------------")
print("1)Молоко - 50 грн")
print("2)Хліб - 30 грн")
print("3)Сік - 70 грн")

try:
    choice = int(input("Оберіть товар - "))
    quantity = int(input("Введіть кількість - "))
    if quantity <= 0 or choice <= 0:
        raise Exception("Quantity and choice must be > 0")
    else:
        if choice == 1:
            product = "Молоко"
            price = 50
        elif choice == 2:
            product = "Хліб"
            price = 30
        elif choice == 3:
            product = "Сік"
            price = 70
        else:
            product = ""
            price = 0
            print("Такого товару немає!")
        if price > 0:
            total = price * quantity
            money = int(input("Введіть суму оплати - "))
            if money >= total:
                change = money - total
                print(f"Product {product}")
                print(f"До сплати {total}")
                print(f"Решта {change}")
            else:
                print("Недостатньо коштів !")
except ValueError:
    print("Enter a number !")
except Exception as ex:
    print(ex)









# Варіант 2 — “Меню кафе”
# Умова
#
# Користувач обирає страву і кількість.
# Якщо сума більше 1000 грн — знижка 10%.
#
# Варіант 3 — “Реєстрація акаунта”
# Умова
#
# Користувач вводить:
#
# логін;
# пароль;
# вік.
#
# Перевірки:
#
# логін не має бути порожнім;
# пароль мінімум 4 символи;
# вік має бути більше 0;
# якщо вік менше 13 — реєстрація заборонена.
