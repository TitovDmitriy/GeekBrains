from task_1_check_date import is_valid_date
from sys import argv

if __name__ == '__main__':
    date_str = argv[1:]
    if is_valid_date(date_str):
        print(f"The date {date_str} is valid.")
    else:
        print(f"The date {date_str} is not valid.")
