"""
Add header to client message
"""
import socket, sys, argparse

PARSER = argparse.ArgumentParser(description='List of available arguments')
PARSER.add_argument('-s', type = int, help = 'size of the buffer')
SIZE = PARSER.parse_args()

print("Initializing....\n")

HOST = '127.0.0.1'
PORT = 65452
CONN = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT_BUFFER_SIZE = SIZE.s
CONN.connect((HOST, PORT))
print("Connected...\n")
print("\nTrying to connect to ", HOST, "(", PORT, ")\n")

BUFFER_SIZE_MSG = CONN.recv(1024)
BUFFER_SIZE_MSG = BUFFER_SIZE_MSG.decode()
SERVER_BUFFER_SIZE = BUFFER_SIZE_MSG.split(':')
SERVER_BUFFER_SIZE = int(SERVER_BUFFER_SIZE[1])
print(BUFFER_SIZE_MSG)
if SERVER_BUFFER_SIZE - 2 != CLIENT_BUFFER_SIZE:
    print('Oops, your buffer size is not equal to the server buffer size')
    sys.exit(0)
MSG_COUNT = 1
TOTAL_MESSAGE = []
while True:
    INPUT_MESSAGE = input("Me: ")
    MESSAGE_TYPE = 'Request'
    MESSAGE = str(INPUT_MESSAGE)
    PROTOCOL_TYPE = 'Py'
    MESSAGE = f'{MESSAGE}'
    MESSAGE_PARTS = [MESSAGE[i:i+CLIENT_BUFFER_SIZE] for  i in range(0, len(MESSAGE), CLIENT_BUFFER_SIZE)]
    for index in range(0, len(MESSAGE_PARTS)):
        FINAL_PART_MSG = ''
        if MESSAGE_PARTS[index] != MESSAGE_PARTS[len(MESSAGE_PARTS) - 1]:
            FINAL_PART_MSG = str(f'{MESSAGE_PARTS[index]}|{MSG_COUNT}')
        else:
            FINAL_PART_MSG = str(f'{MESSAGE_PARTS[index]}')
        CONN.send(FINAL_PART_MSG.encode())
    
   # MESSAGE = CONN.recv(CLIENT_BUFFER_SIZE)
    """MESSAGE = MESSAGE.decode()
    for data in MESSAGE.split('\n'):
        TOTAL_MESSAGE += data
        print("Server: ", TOTAL_MESSAGE)""" 
    """if MESSAGE:
        TOTAL_MESSAGE.append(MESSAGE.decode())
        ''.join(TOTAL_MESSAGE)
        # TOTAL_MESSAGE = TOTAL_MESSAGE.decode()
        print("Server: ", TOTAL_MESSAGE)"""
    # CONN.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFFER_SIZE)
    """SERVER_RES = MESSAGE.strip().split('|')
    MSG_COUNT = SERVER_RES[1]
    MSG_COUNT = int(MSG_COUNT)
    MSG_COUNT += 1"""
    # print("Server: ", MESSAGE)
    if INPUT_MESSAGE == "quit":
        INPUT_MESSAGE = "Left chat room!"
        print("\n")
        break
