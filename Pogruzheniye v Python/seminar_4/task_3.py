MULT = 50
PERCENT = 0.985
EXTRA_PERCENT = 0.97
RICH_PERCENT = 0.9
MIN_CASH = 30
MAX_CASH = 600
MAX_COUNT = 3
MAX_SCORE = 5_000_000
COUNT = 0
TOTAL_SCORE = 0
TEMP_CASH = 0

cash_operations = []  # список операций снятия и пополнения наличных со счёта count_operations = [] # список с количеством снятий и пополнений наличных со счёта


def menu():
    print("Выберите операцию: ")
    while True:
        print("1. Проверить баланс!")
        print("2. Пополнить счёт!")
        print("3. Снять средства!")
        print("4. Завершить сеанс!")
        choice = input("")
        if choice == "1":
            print("Ваш баланс равен: ", balance())
        elif choice == "2":
            add_money(TEMP_CASH, COUNT)
        elif choice == "3":
            remove_money(TEMP_CASH, COUNT)
        elif choice == "4":
            print("До свидания!")
            end_operations()
        else:
            print("Попробуйте снова!")


# Функция пополнения счёта
def add_money(add_cash, COUNT) -> int:
    global TOTAL_SCORE
    print("Укажите сумму для пополнение счёта!")
    add_cash = int(input())
    if add_cash % MULT == 0:
        TOTAL_SCORE += add_cash
        print("Внесение денежных средств прошло успешно")
        cash_operations.append(add_cash)
        COUNT += 1
    else:
        print("Сумма пополнения наличных должна быть кратна 50")


# функция снятия наличных со счёта
def remove_money(remove_cash, COUNT) -> int:
    global TOTAL_SCORE
    print("Укажите сумму для снятия!")
    remove_cash = int(input())
    if remove_cash % MULT == 0 and remove_cash > TOTAL_SCORE:
        print("на вашем счёте недостаточно средств!")
        TOTAL_SCORE -= remove_cash
    elif remove_cash > MAX_SCORE:
        TOTAL_SCORE -= (remove_cash + (remove_cash * RICH_PERCENT))
        print("был вычтен налог на богатство 10%")
        cash_operations.append(-remove_cash * RICH_PERCENT)
        COUNT += 1
    elif remove_cash * PERCENT > MIN_CASH and remove_cash * PERCENT < MAX_CASH:
        TOTAL_SCORE -= remove_cash + (remove_cash * PERCENT)
        print("комиссия за снятие наличных 1.5%")
        cash_operations.append(-remove_cash + (remove_cash * PERCENT))
        COUNT += 1
    elif (remove_cash * PERCENT) < MIN_CASH:
        TOTAL_SCORE -= (remove_cash + MIN_CASH)
        print("комиссия за снятие наличных = 30")
        cash_operations.append(-remove_cash - MIN_CASH)
        COUNT += 1
    elif (remove_cash * PERCENT) > MAX_CASH:
        TOTAL_SCORE -= (remove_cash + MAX_CASH)
        print("комиссия за снятие наличных = 600")
        cash_operations.append(-remove_cash - MAX_CASH)
        COUNT += 1
    else:
        print("Сумма снятия наличных должна быть кратна 50")


if COUNT % MAX_COUNT == 0:
    TOTAL_SCORE *= EXTRA_PERCENT
    COUNT = 0


# функция запроса баланса
def balance():
    return TOTAL_SCORE


def end_operations():
    print(f'все ваши операции в этом сеансе: {cash_operations}')
    exit()


if __name__ == '__main__':
    menu()
