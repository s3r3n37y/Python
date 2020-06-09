# You can esily scan multiple targets with this portscanner. And also import this code in to your future projects. 

import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target]' + str(target))

    for port in range(1,100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(sock):
    return sock.recv(1024).decode('utf-8')

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # setting the timeout for scanning
        sock.connect((ip, port))
        try:
            banner = get_banner(sock)
            print(f"[+] Open port {port}: {banner}")
        except:
            print(f'[+] Open port {port}')
    except:
        pass

if __name__ == "__main__":    
    targets = input('[+] Enter the ip or host to scan: ') # add target by spliting with coma ,
    if ',' in targets:
        for ip in targets.split(','):
            scan(ip.strip(' '))
    else:
        scan(targets)
