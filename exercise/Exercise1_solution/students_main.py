import students_manager as sm
import sys

STUDENTS_FILE_NAME = 'students.txt'
STUDENTS_FINAL_FILE_NAME = 'final_students.txt'
MAX_PASSWORD_TRAILS = 3

if __name__ == '__main__':

    # 1.Read and load the students in runtime memory
    sm.load_students(STUDENTS_FILE_NAME)

    # 2. Prompt for student ID
    student_id = input("Please enter your student ID: ")

    # 3. Check if the student id is valid
    if not sm.is_valid_id(student_id):
        print("The provided student id was not found!")
        sys.exit(1)
    # 4. Prompt for a valid password
    trials = 0
    is_valid_password = False
    user_password = input("Please enter a valid password: ")
    is_valid_password = sm.is_valid_password(user_password)

    while not is_valid_password and trials < MAX_PASSWORD_TRAILS -1:
        user_password = input("Invalid password, please try again: ")
        is_valid_password = sm.is_valid_password(user_password)
        trials += 1
    if not is_valid_password:
        print("You have exhausted your password trials."
              "Please restart again")
        sys.exit(1)

    # 5. Update the student record with the provided password

    student_record = sm.get_student_record(student_id)
    student_record = student_record.replace('\n', '')
    student_record = f'{student_record},password:{user_password}\n'
    if sm.update_final_list(STUDENTS_FINAL_FILE_NAME, student_id, student_record):
        print("Your record was successfully updated!")
    else:
        print("Relax, your record is already up to date!")





