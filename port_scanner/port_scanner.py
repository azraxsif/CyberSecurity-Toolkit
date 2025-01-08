import socket
# low level internetworking library
import threading
# constructs higher level interfaces on the lower level
from datetime import datetime
# to show when the port started scanning from and when the scan was completed


# function to scan a single port
def scan_port(target, port):
    try:
        # create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET = IPv4 and SOCK_STREAM = TCP protocol
        sock.settimeout(1)  # set a timeout for the connection attempt
        result = sock.connect_ex((target, port))
        if result == 0:  # if connection was successful
            try:
                sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
                banner = sock.recv(1024).decode().strip()  # Grab banner (if any)
            except:
              banner = "No banner"
            print(f"[+] Port {port} is OPEN. Banner: {banner}")
            with open("scan_results.txt", "a") as f:
              f.write(f"Port {port} is open\n")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")
        # exception if the code doesnt run


# threaded scanner for faster scanning
def threaded_scanner(target, ports):
    print("\n[INFO] Starting scan...")
    print(f"Target: {target}")
    print(f"Ports: {ports[0]}-{ports[-1]}")
    print(f"Scan started at: {datetime.now()}\n")

    threads = [] # this initializes an empty list to keep track of all the threads created
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target, port)) # creates a new thread of execution
        threads.append(thread) # adds the newly created thread to the threads list.
        thread.start() #restarts the thread
    for thread in threads:
        thread.join() #joins all the previous threads together

    print(f"\n[INFO] Scan completed at: {datetime.now()}")


# resolve hostname to IP and validate
def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"[INFO] Resolved {target} to {ip}")
        return ip
    except socket.gaierror:
        print("[ERROR] Unable to resolve hostname. Exiting...")
        exit(1)


# main function where the code starts
if __name__ == "__main__":
    print("=== Advanced Port Scanner ===")
    target_host = input("Enter target IP or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    ports_to_scan = range(start_port, end_port + 1)

    # resolve target (the ip)
    target_ip = resolve_target(target_host)

    # threaded scanning to keep track of all the ports
    threaded_scanner(target_ip, ports_to_scan)
print("Scanning complete. Results saved to scan_results.txt.")