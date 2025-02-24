import socket

def scan_ports(target, ports):
    open_ports = []
    print(f"Scanning {target} for open ports...\n")
    
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
    
    return open_ports

# Example usage
target_ip = "127.0.0.1"  # Change to target IP
ports_to_scan = [21, 22, 23, 25, 53, 80, 443, 3306]  # Common ports

open_ports = scan_ports(target_ip, ports_to_scan)
print("\nScan complete.")
print("Open ports:", open_ports)
