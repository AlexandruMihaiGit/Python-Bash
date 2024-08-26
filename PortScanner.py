import sys
import socket

#ip = '192.168.1.6'
ip = input("Enter a target!")
open_ports = []

ports = range(1, 1025)

def probe_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # timeout
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

for port in ports:
    if probe_port(ip, port):
        open_ports.append(port)
        print(f" Port {port} is open")
    else:
        print(f" Port {port} is closed", end="\r")

if open_ports:
    print("\n Open Ports are:", sorted(open_ports))
else:
    print("\n Looks like no ports are open :(")
