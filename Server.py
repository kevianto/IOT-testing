import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.159.7",4000))
s.listen()
con,addr=s.accept()
while True:
    data=con.recv(1024)
    d=data.decode()
    print(data)