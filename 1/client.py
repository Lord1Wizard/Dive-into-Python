import socket
import os
import threading

while True:
    try:
        nickname = input("Введите ваш ник: ")
        nickname.encode('ascii')
    except EOFError:
        print("Выход")
        os._exit(1)
    except Exception:
        print("Ошибка: Ввод допускается только на английском языке Ctrl+D-выход")
    else:
        break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except :
            print("Выход")
            client.close()
            break

def write():
    while True:
        try:
            message = '{}: {}'.format(nickname, input(''))
            client.send(message.encode('ascii'))
        except EOFError:
            print("Выход")
            os._exit(1)
        except Exception:
            print("Ошибка: Ввод допускается только на английском языке Ctrl+D-выход")


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

