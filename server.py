import time
import socket
import threading



server = socket.socket()
ip = '192.168.43.82'
port = 12345
server.bind((ip,port))
server.listen()
client,addr = server.accept()




def send(client):
    while True:
        msg = input("-->")
        client.send(msg.encode())
        if msg.lower() == 'bye':
            break
            
def recv(client):
    while True:
        msg = client.recv(1024).decode()
        print(f"by client --> {msg}")
        if msg.lower() == 'bye':
            break
            
send_thread = threading.Thread(target=send,args=(client,))    
recv_thread = threading.Thread(target=recv,args=(client,))
send_thread.start()
recv_thread.start()
send_thread.join()
recv_thread.join()
client.close()
server.close()