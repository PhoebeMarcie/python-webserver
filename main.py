import socket


# step 1: create an initialiser socket
#  socket - endpoint in a network communication system
#  from socket.socket() we use the class socket. 
# class socket(
#     family: AddressFamily | int = -1, - you pass in an IP here (IP - rules for routing/ sending packets of data ) AF_INET is ipV4
#     type: SocketKind | int = -1, - accepts socket kinds eg tcp, when we use  SOCK_STREAM , it's a TCP socket
#     proto: int = -1,
#     fileno: int | None = None
# )

socket.socket(socket.AF_INET)
