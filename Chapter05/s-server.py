import socket
import time

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(5)

try:
	# Echo loop
	while True:
		try:
			newSocket, address = sock.accept()
		except socket.error, (value, message):
			print "Socket error while waiting to accept socket: " + message 
		except:
			print "Unexpected error while waiting to accept"
			break
		print "Connected from echo client ", address
		while True:
			try:
				receivedData = newSocket.recv(1024)
			except socket.error as (value, message):
				print "Socket error while waiting to receive: (value:", value, ") " + message
				break
			except:
				print "Unexpected error while waiting to receive"
				break

			if not receivedData:
			    break
			else:
			    print "Server received: " + receivedData

			newSocket.sendall("I received your data. All ok!")

		# Done transacting with client
		newSocket.close()
		print "Disconnected from", address

except:
	print "Unexpected error in echo loop"
	
finally:
	sock.close()

