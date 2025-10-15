def input_digits_only(s):
    """Возвращает только цифры из строки s."""
    return ''.join(ch for ch in s if ch.isdigit())

def input_with_validation(prompt, length=None):
    """Ввод строки с проверкой на количество цифр, если указана длина."""
    while True:
        value = input(prompt)
        digits = input_digits_only(value)
        if length is not None:
            if len(digits) == length:
                return digits
            else:
                print("Ошибка: нужно ввести ровно",length, "цифр. Повторите ввод.")
        else:
            return value

def input_positive_int(prompt):
    """Ввод положительного целого числа."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Введите положительное целое число.")
        except ValueError:
            print("Некорректный ввод. Введите целое число.")

def menu():
    personal_info = {
        "Имя": "",
        "Возраст": None,
        "Телефон": "",
        "Электронная почта": "",
        "Индекс": "",
        "Почтовый адрес": "",
        "Дополнительная информация": ""
    }

    entrepreneur_info = {
        "ОГРНИП": "",
        "ИНН": "",
        "Расчётный счёт": "",
        "Название банка": "",
        "БИК": "",
        "Корреспондентский счёт": ""
    }

    while True:
        print("\nГлавное меню:")
        print("1 — Ввести или обновить информацию")
        print("2 — Вывести информацию")
        print("0 — Завершить работу")
        choice = input("Введите номер пункта меню: ")

        if choice == '1':
            while True:
                print("\nМеню ввода информации:")
                print("1 — Личная информация")
                print("2 — Информация о предпринимателе")
                print("0 — Назад")
                sub_choice = input("Введите номер пункта меню: ")

                if sub_choice == '1':
                    # Ввод личной информации
                    personal_info["Имя"] = input("Введите имя: ")
                    personal_info["Возраст"] = input_positive_int("Введите возраст (целое число): ")
                    personal_info["Телефон"] = input("Введите телефон: ")
                    personal_info["Электронная почта"] = input("Введите электронную почту: ")

                    index_raw = input("Введите индекс (любая строка с цифрами): ")
                    personal_info["Индекс"] = input_digits_only(index_raw)

                    personal_info["Почтовый адрес"] = input("Введите почтовый адрес: ")
                    personal_info["Дополнительная информация"] = input("Введите дополнительную информацию: ")
                elif sub_choice == '2':
                    # Ввод информации о предпринимателе
                    entrepreneur_info["ОГРНИП"] = input_with_validation("Введите ОГРНИП (15 цифр): ", length=15)
                    entrepreneur_info["ИНН"] = input("Введите ИНН: ")
                    entrepreneur_info["Расчётный счёт"] = input_with_validation("Введите расчётный счёт (20 цифр): ", length=20)
                    entrepreneur_info["Название банка"] = input("Введите название банка: ")
                    entrepreneur_info["БИК"] = input("Введите БИК: ")
                    entrepreneur_info["Корреспондентский счёт"] = input("Введите корреспондентский счёт: ")
                elif sub_choice == '0':
                    break
                else:
                    print("Введён некорректный пункт меню.")

        elif choice == '2':
            while True:
                print("\nМеню вывода информации:")
                print("1 — Личная информация")
                print("2 — Вся информация")
                print("0 — Назад")
                sub_choice = input("Введите номер пункта меню: ")

                if sub_choice == '1':
                    print("\nЛичная информация:")
                    print("Имя:",personal_info['Имя'])
                    print("Возраст:",personal_info['Возраст'])
                    print("Телефон:",personal_info['Телефон'])
                    print("Электронная почта:",personal_info['Электронная почта'])
                    print("Индекс:",personal_info['Индекс'])
                    print("Почтовый адрес:",personal_info['Почтовый адрес'])
                    print("Дополнительная информация:",personal_info['Дополнительная информация'])
                elif sub_choice == '2':
                    print("\nВся информация:")
                    print("Имя:", personal_info['Имя'])
                    print("Возраст:",personal_info['Возраст'])
                    print("Телефон:",personal_info['Телефон'])
                    print("Электронная почта:",personal_info['Электронная почта'])
                    print("Индекс:",personal_info['Индекс'])
                    print("Почтовый адрес:",personal_info['Почтовый адрес'])
                    print("Дополнительная информация:",personal_info['Дополнительная информация'])
                    print("ОГРНИП:",entrepreneur_info['ОГРНИП'])
                    print("ИНН:",entrepreneur_info['ИНН'])
                    print("Расчётный счёт:",entrepreneur_info['Расчётный счёт'])
                    print("Название банка:",entrepreneur_info['Название банка'])
                    print("БИК:",entrepreneur_info['БИК'])
                    print("Корреспондентский счёт:",entrepreneur_info['Корреспондентский счёт'])
                elif sub_choice == '0':
                    break
                else:
                    print("Введён некорректный пункт меню.")

        elif choice == '0':
            print("Завершение работы.")
            break
        else:
            print("Введён некорректный пункт меню.")

menu()