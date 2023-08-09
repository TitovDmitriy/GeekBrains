"""
Задание 2. (повышенной сложности)

Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка 
string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.
"""
import subprocess
import re

def check_output(command, text, mode='default'):
    try:
        output = subprocess.check_output(command, shell=True).decode()
        output_words = re.findall(r'\w+', output.lower())
        if mode == 'default':
            if text in output:
                return True
            else:
                return False
        elif mode == 'word':
            text_words = text.split()
            for word in text_words:
                word = word.lower()
                if word not in output_words:
                    return False
            return True
    except subprocess.CalledProcessError:
        return False


command = "echo 'The quick brown fox jumps over the lazy dog.'"
text = "brown fox jumps"
result = check_output(command, text, mode='word')
print(result)
