"""
Main function to sort and create files
"""
import sorting_manager as sm

INPUT_FILE = 'items.txt'
INPUT_COLUMN = ['sequence', 'size', 'priority']
INPUT_ORDER = ['asc', 'desc']

if __name__ == '__main__':
    # Calling load data function
    raw_data = sm.load_data(INPUT_FILE)
    # Calling function to sort data& Create file
    input_column = input(
        'Please enter a desired columns (Sequence, Size, Priority): ')
    input_order = input('Please enter a desired order (asc or desc): ')
    input_column = input_column.lower()
    input_order = input_order.lower()
    if input_column == 'sequence':
        get_data = sm.get_sorted_data(raw_data, 0, input_order)
        sm.write_files(get_data, input_column)
        print(
            f'Successfully created a {input_column} and {input_order} order file')
    if input_column == 'size':
        get_data = sm.get_sorted_data(raw_data, 1, input_order)
        sm.write_files(get_data, input_column)
        print(
            f'Successfully created a {input_column} and {input_order} order file')
    if input_column == 'priority':
        get_data = sm.get_sorted_data(raw_data, 2, input_order)
        sm.write_files(get_data, input_column)
        print(
            f'Successfully created a {input_column} and {input_order} order file')
    if input_column not in INPUT_COLUMN:
        print('Invalid column input')
