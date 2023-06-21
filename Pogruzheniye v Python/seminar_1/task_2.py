start = 2
final = 10
section = 6

for i in range(start, final):
    for j in range(start, final):
        if j < section:
            print(f'{j} * {i} = {j * i}\t\t', end="")
    print(" ")
print("\n")
for i in range(start, final):
    for j in range(start, final):
        if j >= section:
            print(f'{j} * {i} = {j * i}\t\t', end="")
    print(" ")

