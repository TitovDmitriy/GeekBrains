star = "*"
space = " "
count = 1
row = int(input("Сколько рядов у ёлки?"))
for i in  range(1, row + 1):
    if i == 1:
        print(space * (row - i), star * i)
    else:
        print(space * (row - i), star * i + (star * count))
        count += 1




