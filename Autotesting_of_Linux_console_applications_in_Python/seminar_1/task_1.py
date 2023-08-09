"""
Задание 1.
Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False
в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""
import subprocess

def check_output(command, text):
    try:
        output = subprocess.check_output(command, shell=True).decode()
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False


command = "ls /"
text = "bin"
result = check_output(command, text)
print(result)
