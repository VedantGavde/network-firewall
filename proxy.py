import socket
import ssl
import re

def extract_hostname(text): #Extracts hostnames from packets

    regex = r'www\.[^.]+\.com' #Can't do this, this does not identify domains such as store.steampowered.com or www.sci-hub.org
    extracted_hostname = re.search(regex, text) #Handle AttributeError for NoneType object if no URL is detected
    return extracted_hostname.group()


def setup_listener(port, certfile, keyfile): #Initializes an SSL wrapped listener 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) 
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"Server listening on https://localhost:{port}...")
    return server_socket
    
def handle_connect(listener_socket): #Handles CONNECT (always first packet when using a proxy) request from client to proxy
    
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile, keyfile)
    client_socket, client_address = listener_socket.accept()
    listener_socket.close()
    print(f"Connection received from {client_address[0]}:{client_address[1]}")
    request = client_socket.recv(buffer_size)
    hostname = extract_hostname(request.decode('utf-8'))
    print(f"Client is trying to connect to {hostname}")
    client_socket.send('HTTP/1.1 200 Connection Established\r\n\r\n'.encode())
    client_socket = ssl_context.wrap_socket(client_socket, server_side=True)
    client_socket.do_handshake()
    return hostname, client_socket
    	

def connect_server(hostname): #Performs proxy to server connection based on provided hostname, uses destination port 443

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    server_socket = ssl_context.wrap_socket(server_socket, server_hostname=hostname)   
    server_socket.connect((hostname, 443))
    return server_socket
    

def proxying(client_socket, server_socket): #Forwards packets between client and the server
    	
    print("Starting proxy communication...")
    client_socket.settimeout(1)
    #client_socket.setblocking(0)
    server_socket.settimeout(1)
    #server_socket.setblocking(0)
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
        except:
            print("Server socket timed out!")
    print("Communication complete!")
    client_socket.close()
    server_socket.close()
    

buffer_size = 4096
port = 8080
port_server = 443
certfile = 'certificate.crt'  
keyfile = 'private.key'

listener_socket = setup_listener(port, certfile, keyfile)
while True:
    hostname, client_socket = handle_connect(listener_socket)
    server_socket = connect_server(hostname)
    proxying(client_socket, server_socket)




