"""
Process to run server which receives string from the server
and create files based on the input
"""
import socket
import file_manager as fm

FILE_NAME = './final_students.txt'
FILE_FORMAT = ['CSV', 'JSON', 'XML']

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server listening...')
    CONN, ADDR = s.accept()
    with CONN:
        print('Connect by', ADDR)
        while True:
            DATA = CONN.recv(1024).decode()
            if not DATA:
                break
            INPUT_TEXT = DATA.upper()

            if INPUT_TEXT == 'JSON':
                fm.load_data_json(FILE_NAME)
            if INPUT_TEXT == 'CSV':
                fm.load_data_csv(FILE_NAME)
            if INPUT_TEXT == 'XML':
                fm.load_data_xml(FILE_NAME)
            if INPUT_TEXT not in FILE_FORMAT:
                print("File extension is not supported!")
