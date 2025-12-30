import socket 

def scan_udp(host, ports, timeout=1):

    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
                s.settimeout(timeout)
                s.sendto(b"", (host, port))
                data, addr = s.recvfrom(1024)
                open_ports.append(port)
        except :
            pass
    return open_ports
