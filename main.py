from modules.tcp_scanner import scan_tcp_port
from modules.udp_scanner import scan_udp
from modules.service import detect_service
from modules.banner import grab_banner
from modules.vulnerability_check import vulnerability_check

def scan(host,ports,scan_type):

    if not ports:
        ports = range (1,1025)

    if scan_type == "tcp":
        tcp = scan_tcp_port(host,ports)
        if not tcp:
            print("No open TCP ports found")
            return

        print(f"Found {len(tcp)} open TCP ports ")

        for port in tcp:
            service = detect_service(port)
            banner = grab_banner(host, port)
            vulns = vulnerability_check(port, banner or "")
            print(f"Service: {service} \n Banner:{banner if banner else 'no banner found'} \n Vulnerabilities: {vulns if vulns else 'No vulnerabilities detected'}")


    if scan_type == "udp":
        udp = scan_udp(host,ports)

        if not udp:
            print("No open UDP ports found ")
            return
        
        print(f"Found {len(udp)} open UDP ports ")

        for port in udp:
            service = detect_service(port)
            banner = grab_banner(host, port)
            vulns = vulnerability_check(port, banner or "")
            print(f"Service: {service} \n Banner:{banner if banner else 'no banner found'} \n Vulnerabilities: {vulns if vulns else 'No vulnerabilities detected'}")



host = input("Enter the host address: ")
ports = input("enter port range: ")
scan_type = input("enter type of scan (tcp or udp): ")

if '-' in ports:
    start_port, end_port = map(int, ports.split('-'))
    ports = range(start_port, end_port + 1)
else:
    ports = [int(ports)]

scan(host,ports,scan_type)