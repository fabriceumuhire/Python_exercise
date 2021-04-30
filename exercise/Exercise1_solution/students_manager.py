import re

PART_SEPARATOR = ','
VALUE_SEPARATOR = ':'
MIN_PASSWORD_LENGTH = 8
students_records = {}

def load_students(file_name):
    try:
        with open(file_name, 'r') as students:
            for student in students:
                id_part = student.strip().split(PART_SEPARATOR)
                id_value = id_part[0].strip().split(VALUE_SEPARATOR)[1]
                students_records.update({id_value : student})
    except FileNotFoundError:
        pass

def is_valid_id(student_id : str) -> bool:
    if students_records.get(student_id):
        return True
    return False

def get_student_record (student_id : str) -> str:
    return students_records.get(student_id)

def is_valid_password(password : str) -> bool:
    reserved_characters = ['!', '+', '=']
    password_copy = password
    regex = '^[0-9A-Za-z]+$'
    if len(password) < MIN_PASSWORD_LENGTH:
        return False
    for character in password:
        if character in reserved_characters:
            return False
        elif not character.isalnum():
            password_copy = password_copy.replace(character, '', 1)
    if len(password_copy) == len(password):
        return False
    if re.search(regex, password_copy):
        return True
    return False

def is_record_updated(file_name : str, student_id : str) -> bool:
    try:
        with open(file_name, 'r') as final_file:
            for record in final_file:
                if record.startswith(f'id:{student_id}'):
                    return True
    except FileNotFoundError:
        pass
    return False

def update_final_list(file_name : str, student_id : str, student_record : str) -> int:
    if is_record_updated(file_name, student_id):
        return 0
    try:
        with open(file_name, 'a') as final_file:
            final_file.write(student_record)
    except FileNotFoundError:
        return 0
    return 1
