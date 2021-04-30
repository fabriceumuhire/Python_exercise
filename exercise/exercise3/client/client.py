"""
Process to run client which sends string to the server
"""
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    INPUT_EXT = input("Provide desired file extension: ")
    s.send(INPUT_EXT.encode())
    s.close()
