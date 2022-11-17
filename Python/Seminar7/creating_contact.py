def new_contact():
    surname = input("Введите Фамилию: ")
    name = input("Введите Имя: ")
    phone_number = str(input("Введите номер телефона: "))
    description = input("Введите описание: ")
    contact_data = [surname, name, phone_number, description]
    return contact_data

nc = []
nc = new_contact()


