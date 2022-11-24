from sorting_file import sorting, get_data
from interface import info_input, select_operation
from interaction_file import read_file, write_file
from working_with_data import working_data


def front():
    return working_data(select_operation, read_file, write_file, sorting, get_data, info_input)
