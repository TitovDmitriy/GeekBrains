# Task4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример
# 	а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

file = open('C:\GitHub_projects\GB\Python\Seminar5\data_for_compression.txt', 'r') 
data = file.read()
file.close()
print(data)

def encode(symbols):
    result = ""
    preChar = ''
    count = 1
    for index, char in enumerate(symbols):
        if index == 0:
            preChar = char
            continue

        if preChar == char:
            count += 1
            if index == len(symbols)-1:
                result += f"{count}{preChar}"
        else:
            if index != len(symbols)-1:
                result += f"{count}{preChar}"
                count = 1
            else:
                result += f"{count}{preChar}1{char}"        
        preChar = char
    return result

compression = encode(data)
print(compression)

f = open('C:\GitHub_projects\GB\Python\Seminar5\RLE.txt', 'w')
f.write(compression) 
f.close()