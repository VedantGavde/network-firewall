import socket
import ssl

def proxy_server():
    # Set up the socket connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(1)

    print("Proxy server is listening on port 8888")

    while True:
        # Accept incoming connections from clients
        client_socket, client_address = server_socket.accept()
        print("Received connection from {client_address[0]}:{client_address[1]}")

        # Receive client request and extract target server's hostname and port number
        request = client_socket.recv(4096)
        #print(request)
        hostname = request.decode().split("//")[1].split("/")[0]
        print(hostname)
        port = 80

        # Establish a connection with the target server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((hostname, port))
        print("Connection with server established!")

        # Send the client's request to the server
        server_socket.sendall(request)
        print(request)
        print("Client's request sent to the server!")

        # Receive the server's response
        while True:
        	response = server_socket.recv(1024)
        	if not response:
        		break
        	client_socket.sendall(response)
        
       '''response = server_socket.recv(4096)
        print("This is the server's response!")
        print(response)

        # Send the server's response back to the client
        client_socket.sendall(response)'''

        # Close the connections
        server_socket.close()
        client_socket.close()

if __name__ == "__main__":
    proxy_server()

