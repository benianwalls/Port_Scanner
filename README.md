# Simple TCP Port Scanner (learning)
A beginner-friendly Python Port scanner that performs basic port scanning in python
Repository contains:
- "scanner.py" - the original scanner class (portScanner) that uses socket and ThreadPoolExecutor.
## Features
- Tests TCP connectivity with socket.connect_ex.
- Prints port states: open, closed, or filtered.
- Uses concurrent.futures.ThreadPoolExecutor to perform scans in parallel.
- Example unit tests that mock sockets (no real network access required).