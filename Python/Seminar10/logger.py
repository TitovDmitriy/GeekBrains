from datetime import datetime as dt

def log_info(data):
    time = dt.now().strftime('%D %H:%M')
    with open('C:\GitHub_projects\GB\Python\Seminar10\log.txt', 'a') as file:
        file.write(f'{time} info: {data}\n')

