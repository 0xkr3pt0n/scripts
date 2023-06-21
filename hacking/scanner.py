import socket
import sys
from datetime import datetime
import threading

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4
else:
    print("Invalid Arguments")
    print("Usage: python3 scanner.py <ip> or python3 scanner.py www.example.com")
    sys.exit()

# banner
print("-" * 50)
print("Scanning Target: " + target)
start_time = datetime.now() # record start time
print("Time Started: " + str(datetime.now()))
print("-" * 50)

# Define a function to scan a single port
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()

# Create a list of ports to scan
ports = range(0, 65535)

# Create a thread for each port and start them
threads = []
for port in ports:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
end_time = datetime.now() # record end time
print("Scanning Completed")
print("Time Taken: " + str(end_time - start_time)) # print elapsed time