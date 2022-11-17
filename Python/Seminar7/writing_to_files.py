from creating_contact import nc
data_lst = []
data_lst = nc
def writing_to_scv():
    file = 'C:\GitHub_projects\GB\Python\Seminar7\Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{data_lst[0]}; {data_lst[1]}; {data_lst[2]}; {data_lst[3]}\n\n')
        data.close()

def writing_to_txt():
    file = 'C:\GitHub_projects\GB\Python\Seminar7\Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {data_lst[0]}\nИмя: {data_lst[1]}\nНомер телефона: {data_lst[2]}\nОписание: {data_lst[3]}\n\n')
        data.close

