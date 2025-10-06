import socket   
import sys
#def function, target= ip address, ports= list of ports
def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...")
    #Empty list to hold open ports
    open_ports = []
    for port in ports:
        # socket af_inet = ipv4, sock_stream = tcp
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt, so doenst loop
        sock.settimeout(1)  
        # 0 means success, anything else is failure
        result = sock.connect_ex((target, port))
        if result == 0:
            #if successful, add to open ports list
            open_ports.append(port)
        # Close the socket after checking each port
        sock.close()
    return open_ports

#def grab_banner(target, port):