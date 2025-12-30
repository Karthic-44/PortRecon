import socket 

def scan_tcp_port(host, ports, timeout=1):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
        except:
            pass
    return open_ports