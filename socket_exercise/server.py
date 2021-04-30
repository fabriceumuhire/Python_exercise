"""
Add header to server message
"""
import socket


print("Initializing....\n")

HOST = '127.0.0.1'
PORT = 65452
SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER_SIZE = 7
SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, BUFFER_SIZE)
SOCK.bind((HOST, PORT))
print(HOST, "(", HOST, ")\n")

SOCK.listen()
CONN, ADDR = SOCK.accept()
print("Received connection from ", ADDR[0], "(", ADDR[1], ")\n")
BUFFER_SIZE_MSG = f'Server buffer size: {BUFFER_SIZE}'
CONN.send(BUFFER_SIZE_MSG.encode())
CLIENT_MESSAGE = ''
MSG_COUNT = 1
while True:
    MESSAGE = CONN.recv(BUFFER_SIZE)
    MESSAGE = MESSAGE.decode()
    RCVD_MESSAGE = MESSAGE.split('|')
    
    try:
        if MSG_COUNT == int(RCVD_MESSAGE[1]):
            CLIENT_MESSAGE += RCVD_MESSAGE[0]
        if RCVD_MESSAGE[1] is None:
            continue
    except IndexError:
        print("Client: ", CLIENT_MESSAGE)
    # print("====",RCVD_MESSAGE[1])
    
    """INPUT_MESSAGE = input(str("Me: "))
    PROTOCOL_TYPE = RCVD_MESSAGE[0]
    if PROTOCOL_TYPE != 'Py':
        break
    MESSAGE_ID = RCVD_MESSAGE[1]
    MESSAGE_TYPE = 'Response'
    MESSAGE = f'{PROTOCOL_TYPE}|{MESSAGE_ID}|{MESSAGE_TYPE}|{INPUT_MESSAGE}'"""
    '''if INPUT_MESSAGE == "quit":
        INPUT_MESSAGE = "Left chat room!"
        CONN.send(INPUT_MESSAGE.encode())
        print("\n")
        break'''
    # CONN.sendall(MESSAGE.encode())
