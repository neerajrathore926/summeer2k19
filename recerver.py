#!usr/bin/python2

import socket

recv_ip="127.0.0.1"
recv_port=4444 # 0- 1024 -- you can check free udp port netstat -nulp

# creating udp socket
#    ip type v4 , uDp
s=socket.soclrt(Isocket.AF_INET,socket.DOCK_DGRAM)
#  fitting ip  and port with udp socket 
s.bind((recv-ip,recv_port))
#    recv data from sender 
data=s.recvfrom(100)
print(data)
