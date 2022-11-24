def get_data(x, y):
    lst = []
    for i in y:
        lst.append(i.split()[x])
    return lst


def sorting(x, y):
    lst = []
    for i in y:
        if x in i:
            lst.append(i)
    return lst
