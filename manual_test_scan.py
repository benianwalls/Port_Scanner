# manual_test_scan.py
from scanner import scan_ports  # adjust if your module name differs
#test to scan manual http server on localhost
def main():
    target = "127.0.0.1"
    # choose ports: include ones we expect open (8000, 50000) and closed ones (9999)
    ports = [22, 80, 8000, 50000, 9999]
    open_ports = scan_ports(target, ports)
    print("=== TEST RESULT ===")
    print(f"Scanned {target} ports: {ports}")
    print(f"Open ports found: {open_ports}")

if __name__ == "__main__":
    main()