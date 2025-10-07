#imports
import socket   
from concurrent.futures import ThreadPoolExecutor
#def function, target= ip address, ports= list of ports

class portScanner():
    def __init__(self):
        pass
    @staticmethod
    def portScanner(target, port):

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                #open port
                if result == 0:
                    print(f"Port: {port} is open")
                #closed ports
                elif result in [111,113]:
                    print(f"Port: {port} is closed")
                #filtered port
                else:
                    print(f"Port: {port} is filtered")


        except Exception as e:
            print(f"Exception Error: {e}")
        
    def threader(target, thread_count=500):
        #Will be responsible for creating multiple threads, paralle scanning
        ports = [20,21,22,23,25,53,80,110,143,443,995,3389]
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            for port in ports:
                executor.submit(portScanner.portScanner, target, port)
            executor.shutdown(wait=True)
            print("Port Scanning Completed")
    def main():
        #Perfoming class wide logic
        choice = input("Enter target domain ").strip().lower()
        target = socket.gethostbyname(choice)
        portScanner.threader(target=target)
        
if __name__ == "__main__":
    portScanner.main()
    