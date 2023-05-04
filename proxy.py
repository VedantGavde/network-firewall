import socket
import ssl
import re

def extract_hostname(text): #Extracts hostnames from packets

    regex = r'www\.[^.]+\.com' #Can't do this, this does not identify domains such as store.steampowered.com or www.sci-hub.org
    extracted_hostname = re.search(regex, text) #Handle AttributeError for NoneType object if no URL is detected
    return extracted_hostname.group()


def setup_listener(port, certfile, keyfile):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) 
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind(('localhost', port))
    client_socket.listen(1)
    print(f"Server listening on https://localhost:{port}...")
    return client_socket
    
def receive_connection(listener_socket):
    
    client_socket, client_address = listener_socket.accept()
    listener_socket.close()
    print(f"Connection received from {client_address[0]}:{client_address[1]}")
    return client_socket, client_address
    
    
def get_hostname(client_socket):
    request = client_socket.recv(buffer_size)
    hostname = extract_hostname(request.decode('utf-8'))
    print(f"Client is trying to connect to {hostname}")
    return hostname
    
def handle_CONNECT(client_socket, server_ip, destination_port)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    server_socket = ssl_context.wrap_socket(server_socket, server_hostname=hostname)   
    server_socket.connect((server_ip, destination_port))
    print(f"Connection established with the server at {server_ip}:{destination_port}") 
    client_socket.send('HTTP/1.1 200 Connection Established\r\n\r\n'.encode())
    
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile, keyfile)
    client_socket = ssl_context.wrap_socket(client_socket, server_side=True)
    client_socket.do_handshake()
    return client_socket, server_socket
    

def proxying(client_socket, server_socket): #Forwards packets between client and the server
    	
    print("Starting proxy communication...")
    client_socket.settimeout(1)
    server_socket.settimeout(1)
    while True:
        try:
            while True:
                request = client_socket.recv(1024)
                if not request: break
                print(f"REQUEST: \n\n{request}")
                server_socket.sendall(request)
                print("Request sent!")
        except socket.timeout:
            print("Client socket timed out!")
        
        try:
            while True:
                response = server_socket.recv(1024)
                if not response: break
                print(f"RESPONSE: \n\n{response}")
                client_socket.sendall(response)
                print("Response received!")
        except socket.timeout:
            print("Server socket timed out!")
    print("Communication complete!")
    client_socket.close()
    server_socket.close()
    



