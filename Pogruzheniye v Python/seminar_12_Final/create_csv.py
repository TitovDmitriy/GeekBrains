import csv

subjects = ["Математика", "Физика", "История"]

# Записываем данные в файл
with open("subjects.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    for subject in subjects:
        writer.writerow([subject])
