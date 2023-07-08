import re


def is_leap_year(year):
    # Проверяем, является ли год високосным.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(date_str):
    # Проверяет, может ли дата существовать.
    # Принимает входную дату в формате DD.MM.YYYY.
    # Возвращает True, если дата может существовать, и False, если не может.
    match = re.match(r'^(\d{2})\.(\d{2})\.(\d{4})$', date_str)
    if not match:
        return False
    day, month, year = map(int, match.groups())
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month == 2:
        if day > 29:
            return False
        if day == 29 and not is_leap_year(year):
            return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    return True


if __name__ == '__main__':
    print(is_valid_date("31.02.2022"))
    print(is_valid_date("29.02.2020"))
    print(is_valid_date("30.04.2022"))
    print(is_valid_date("31.06.2022"))
    print(is_leap_year(2020))
