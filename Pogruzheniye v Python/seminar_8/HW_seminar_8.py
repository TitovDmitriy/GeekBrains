import os
from file_formats import to_json, to_csv, to_pickle


def process_directory(directory):
    data = []

    for root, dirs, files in os.walk(directory):
        # Рассчитываю размер файла или директории
        size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
        size += sum(os.path.getsize(os.path.join(root, name)) for name in dirs)

        # Создаю запись для каждого файла
        for file in files:
            file_path = os.path.join(root, file)
            record = {
                "name": file,
                "type": "file",
                "size": os.path.getsize(file_path)
            }
            data.append(record)

        # Создаю запись для каждой директории
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            record = {
                "name": dir,
                "type": "directory",
                "size": sum(os.path.getsize(os.path.join(dir_path, name)) for name in os.listdir(dir_path))
            }
            data.append(record)

    # Сохранение данных в разных форматах
    to_json(data, 'directory_data.json')
    to_csv(data, 'directory_data.csv')
    to_pickle(data, 'directory_data.pickle')


process_directory('C:\GitHub_projects\GB\Pogruzheniye v Python\seminar_8\file_formats')
