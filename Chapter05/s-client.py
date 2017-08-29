import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8888))
print "Connected to echo server"
try:
    sock.sendall("Hello there!")
    try:
        response = sock.recv(1024)
    except socket.error as (value, message):
        print "Socket error while waiting to receive: (value:", value, ") " + message
    except:
        print "Unexpected error"

    print "Received:", response
except:
	print "Unexpected error in echo loop"

sock.close()

