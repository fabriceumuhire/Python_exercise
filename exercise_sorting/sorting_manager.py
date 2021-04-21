"""
Below functions are for exercise for sorting
"""


def load_data(file_name):
    """
    Function for loading data
    """
    try:
        with open(file_name, 'r') as raw_data:
            data = []
            for items in raw_data:
                lines = list(items.strip().split(' '))
                lines[0] = int(lines[0])
                lines[1] = int(lines[1])
                data.append(lines)
        return data
    except FileNotFoundError as error:
        print(error)


def get_sorted_data(input_data, user_type, user_order):
    """
    Function for get data in both ascending and descending
    """
    if user_order == 'asc':
        sorted_data = sorted(
            input_data, key=lambda line: line[user_type], reverse=True)
    elif user_order == 'desc':
        sorted_data = sorted(input_data, key=lambda line: line[user_type])
    return sorted_data


def write_files(sorted_data, input_column):
    """
    Function for write data
    """
    try:
        with open(f'order_by_{input_column}.txt', 'w') as txt_file:
            for item in sorted_data:
                raw_data = ' '.join([str(elem) for elem in item])
                txt_file.write(str(raw_data) + '\n')
            return
    except FileNotFoundError as error:
        print(error)
