# Напишите однострочный генератор словаря, который принимает на вход три
# списка одинаковой длины: имена str, ставка int, премия str с указанием процентов
# вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент
# премии
def calculate_bonus(names, salary, bonus_percents):
    bonus_dict = {}
    for name, sal, bonus in zip(names, salary, bonus_percents):
        bonus_percent = float(bonus[:-1])
        bonus_amount = sal * bonus_percent / 100
        bonus_dict[name] = bonus_amount
    return bonus_dict


names = ["Alice", "Bob", "Charlie"]
salary = [100, 200, 300]
bonus_percents = ["10.25%", "5.5%", "3%"]
bonus_dict = calculate_bonus(names, salary, bonus_percents)
print(bonus_dict)
