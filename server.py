import socket
import threading
import queue

mesaje = queue.Queue()
clienti = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 7777))

def primire():
    while True:
        try:
            mesaj,adr = server.recvfrom(1024)
            mesaje.put((mesaj,adr))
        except:
            pass

def afisare():
    while True:
        while not mesaje.empty():
            mesaj,adr = mesaje.get()
            print(mesaj.decode())
            if adr not in clienti:
               clienti.append(adr)
            for client in clienti:
                try:
                    if mesaj.decode().startswith('SIGNUP_TAG:'):
                        nume = mesaj.decode()[mesaj.decode.index(':') + 1:]
                        server.sendto(f'{nume} joined'.encode(), client)
                    else:
                        server.sendto(mesaj, client)
                except:
                   clienti.remove(client)


t1 = threading.Thread(target=primire)
t2 = threading.Thread(target=afisare)

t1.start()
t2.start()

print('Chat-ul este deschis ...')