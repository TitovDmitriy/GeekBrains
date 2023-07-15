import csv
import pickle


def csv_to_pickle(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # считываю заголовки

        for row in reader:
            record = {}  # создаю словарь для текущей строки
            for index, value in enumerate(row):
                record[headers[index]] = value
            data.append(record)
    # преобразовываю данные в строку pickle
    pickle_string = pickle.dumps(data)

    print(pickle_string)


csv_to_pickle('users.csv')
