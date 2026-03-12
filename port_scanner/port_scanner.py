import socket



def scan(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    ergebnis = sock.connect_ex((ip, port))

    try:

         return ergebnis == 0
    finally:
        sock.close()



