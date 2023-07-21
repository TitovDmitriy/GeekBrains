import csv
import json


class CSVProcessor:
    def __init__(self, csv_file, json_file):
        self.csv_file = csv_file
        self.json_file = json_file
        self.data = []

    def process_csv(self):
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                id = row[0].zfill(10)
                name = row[1].capitalize()
                access_level = int(row[2])
                hash = name + id

                record = {
                    "id": id,
                    "name": name,
                    "access_level": access_level,
                    "hash": hash
                }
                self.data.append(record)

        with open(self.json_file, 'w') as file:
            json.dump(self.data, file, indent=4)

        print(f"Данные успешно сохранены в файл {self.json_file}!")


processor = CSVProcessor('users.csv', 'users.json')
processor.process_csv()
