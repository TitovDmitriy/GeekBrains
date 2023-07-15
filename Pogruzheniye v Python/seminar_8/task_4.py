import csv
import json


def process_csv(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовки

        for row in reader:
            id = row[0].zfill(10)  # Дополнение id нулями до 10 цифр
            name = row[1].capitalize()  # Преобразование первой буквы имени в прописную
            access_level = int(row[2])
            hash = name + id  # Создание хеша на основе имени и идентификатора

            record = {
                "id": id,
                "name": name,
                "access_level": access_level,
                "hash": hash
            }
            data.append(record)

    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Данные успешно сохранены в файл {json_file}!")


process_csv('users.csv', 'users.json')
