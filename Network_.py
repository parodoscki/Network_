import socket
from _thread import *
from logging import raiseExceptions


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = "hello"
    while True:
        try:
            data = conn.recv(2048)
            recv_d = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", recv_d)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break
            print("Lost connection")
            conn.close()
class Network:
    def __init__(self,port,ip):
        self.port = port
        self.ip = ip
        self.addr = (self.ip,self.port)
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def connect(self):
        try:
          self.client.connect(self.addr)
          print('Connected.')
        except socket.error as e:
          print(e)
    def send(self,data):
        try:
          self.client.send(data.encode())
        except:
          print('error trying to send a message')
    def recieve(self):
        data = self.client.recv(2028)
        return data.decode()
class Server:
    def __init__(self,ip,port,client_amount):
        self.ip = ip
        self.port = port
        self.amount = client_amount
        self.port = port
        self.addr = (self.ip,self.port)
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind(self.addr)
        self.server.listen(self.amount)
        self.conn, self.addr_c = None,None
    def connect_server(self):
        global conn,addr_c
        self.conn, self.addr_c = self.server.accept()
    def find(self):
        start_new_thread(threaded_client,(self.conn,))
    def recieve(self):
        try:
          return self.server.recv(2028).decode('utf-8')
        except socket.error:
            return self.server.recv(2028).decode('utf-8')