import socket

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Attempt to connect to `host` on TCP `port`.
    Returns True if the port is open, False otherwise.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False

def main():
    host_input = input("Enter host (IP or domain): ").strip()
    try:
        # Resolve domain to IP; throws socket.gaierror if invalid
        host = socket.gethostbyname(host_input)
    except socket.gaierror:
        print(f"Invalid host: {host_input}")
        return

    # Define the port range
    start_port = 1
    end_port = 1024

    print(f"Scanning {host} (resolved from {host_input}) for ports {start_port}-{end_port}...\n")

    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"[+] Port {port} is open")
            open_ports.append(port)
        # Optional: Uncomment to see closed ports
        # else:
        #     print(f"[-] Port {port} is closed")

    if open_ports:
        print("\nScan complete! Open ports:")
        for port in open_ports:
            print(f"  - {port}")
    else:
        print("\nScan complete! No open ports found in the specified range.")

if __name__ == "__main__":
    main()
