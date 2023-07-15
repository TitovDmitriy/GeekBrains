import pickle
import csv


def pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as file:
        data = pickle.load(file)

    # Извлечение заголовков столбцов из ключей словаря
    headers = set()
    for row in data:
        headers.update(row.keys())

    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"Данные успешно сохранены в файл {csv_file}!")


pickle_to_csv('users.pickle', 'users.csv')
