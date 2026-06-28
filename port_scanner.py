import socket
import threading
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init()

target = input(f"{Fore.CYAN}Enter IP address to scan: {Style.RESET_ALL}")

def get_service(port):
    services = {
        21: "FTP", 22: "SSH", 23: "Telnet",
        25: "SMTP", 53: "DNS", 80: "HTTP",
        110: "POP3", 443: "HTTPS", 3306: "MySQL",
        8080: "HTTP-Alt"
    }
    return services.get(port, "Unknown")

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            service = get_service(port)
            print(f"{Fore.GREEN}  Port {port} is OPEN ✅ ({service}){Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}  Port {port} is CLOSED ❌{Style.RESET_ALL}")
        sock.close()
    except:
        pass

print(f"\n{Fore.YELLOW}Scanning {target} ...{Style.RESET_ALL}")
print(f"Started at: {datetime.now()}\n")

threads = []
for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\n{Fore.CYAN}Scan complete! ✅{Style.RESET_ALL}")