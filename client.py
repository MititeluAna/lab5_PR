import socket
import threading
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('localhost', random.randint(8000, 9000)))

nume = input('Nickname: ')

def primire():
    while True:
        try:
            mesaj, _ = client.recvfrom(1024)
            print(mesaj.decode())
        except:
            pass

r = threading.Thread(target=primire)
r.start()

client.sendto(f'SIGNUP_TAG:{nume}'.encode(), ('localhost', 7777))

while True:
    mesaj = input('')
    if mesaj == '!q':
        exit()
    else:
        client.sendto(f'{nume}: {mesaj}'.encode(), ('localhost', 7777))
