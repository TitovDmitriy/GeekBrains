def working_data(number, read, write, sort, data, data_data):
    while True:
        d = number()
        if d == "0":
            print(*data(0, read()), sep="\n")
        elif d == "1":
            print(*data(1, read()), sep="\n")
        elif d == "2":
            print(*data(2, read()), sep="\n")
        elif d == "3":
            print(*data(3, read()), sep="\n")
        elif d == "4":
            print(*data(4, read()), sep="\n")
        elif d == "5":
            print(*sort(input("Введите описание карточки сотрудника: ").lower(), read()), sep="")
        elif d == "6":
            print(*read(), sep="")
        elif d == "7":
            print(*sort(input("Введите фамилию сотрудника: "), read()), sep="")
        elif d == "8":
            write(data_data())
        elif d == "9":
            print("Работа с системой завершена!")
            break
