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
       # Get custom port range from the user
    try:
        start_port = int(input("Enter start port (e.g. 1): ").strip())
        end_port   = int(input("Enter end port   (e.g. 1024): ").strip())
        if start_port < 1 or end_port < start_port or end_port > 65535:
            raise ValueError
    except ValueError:
        print("Invalid port range. Please enter integers: 1 ≤ start ≤ end ≤ 65535.")
        return


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
