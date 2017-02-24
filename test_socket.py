import network #needed currently for ESP32 socket instantiation
import socket
import errno

SOCKET_TIMEOUT = 10.0
MY_ESSID = "dolphnet"
MY_PW    = "mcmlxix1969"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(MY_ESSID,MY_PW)

while not sta_if.isconnected():
    print("\twaiting for WLAN to connect")
    time.sleep(1.0)

ifconfig = sta_if.ifconfig()
print(ifconfig)

host = ifconfig[0]
addr = socket.getaddrinfo(host,80)[0][-1]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(SOCKET_TIMEOUT)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("binding socket to addr:",addr)
sock.bind(addr)
sock.listen(5)


while True:
    client_sock = None
    try:
        print("Waiting for connection...")
        client_sock, client_address = sock.accept()
        print("accepted connection from '%s'" % (client_address,))
    except OSError as exc:
        if exc.args[0] == errno.ETIMEDOUT:    #case for ESP8266
            print("Caught OSError: ETIMEDOUT")
        elif exc.args[0] == errno.EAGAIN:     #case for ESP32
            print("Caught OSError: EAGAIN")
        else:
            raise
    finally:
        if client_sock:
            client_sock.close()
