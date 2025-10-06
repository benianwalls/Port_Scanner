#imports
import socket   
from concurrent.futures import ThreadPoolExecutor
#def function, target= ip address, ports= list of ports

class portScanner():
    def __init__(self):
        pass
    def portScanner(target, port):

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                #open port
                if result == 0:
                    print(f"Port: {port} is open")
                #Filtered ports
                elif result in [111,113]:
                    print(f"Port: {port} is filtered")
                #closed port
                else:
                    print(f"Port: {port} is closed")


        except Exception as e:
            print(f"Exception Error: {e}")
   