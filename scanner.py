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

