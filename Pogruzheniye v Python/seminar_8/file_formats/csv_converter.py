import csv


def to_csv(data, file_path):
    if len(data) == 0:
        return

    headers = data[0].keys()
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
