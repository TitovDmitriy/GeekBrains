def write_file(data):
    with open('C:\GitHub_projects\GB\Python\Seminar8\Database.txt', 'a', encoding = 'utf-8') as file:
        file.writelines(data)
          
def read_file():
    with open('C:\GitHub_projects\GB\Python\Seminar8\Database.txt','r', encoding = 'utf-8') as file:
        return file.readlines()


