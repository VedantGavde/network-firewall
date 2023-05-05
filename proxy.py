import socket
import ssl
import re
import sys
import url_filter

proxy_certificate = './../certificate.crt'  
proxy_private_key = './../private.key'

def extract_hostname(request): #Extracts hostnames from packets

    if "CONNECT" in request:
        # Extract URL from CONNECT request
        url_start = request.find("CONNECT") + 8
        url_end = request.find("HTTP/1.1") - 1
        url = request[url_start:url_end]
        filtered_url = url.split(":")[0]
        server_port = url.split(":")[1]
        print("URL from CONNECT request:", filtered_url)
        return filtered_url, server_port
    else:
        print("Could not find CONNECT in the request")
        sys.exit()
    
def extract_url(request):
    if "GET" in request:
        # Extract URL from GET request
        path_start = request.find("GET") + 4
        path_end = request.find("HTTP/1.1") - 1
        path = request[path_start:path_end]
        url_start = request.find("Host:") + 6
        url = request[url_start:]
        url_end = url.find("\r\n")
        url = url[:url_end]
        url = "https://" + url + path
        print("URL from GET request:", url)
        return url


def setup_listener(port):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) 
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind(('localhost', port))
    client_socket.listen(1)
    print(f"Server listening on https://localhost:{port}...")
    return client_socket
    
def receive_connection(listener_socket):
    
    try:    
        client_socket, client_address = listener_socket.accept()
    except OSError:
        sys.exit()     
    #finally:    
        #listener_socket.close()
    print(f"Connection received from {client_address[0]}:{client_address[1]}")
    return client_socket, client_address
    
    
def get_hostname(client_socket):
    request = client_socket.recv(4096)
    hostname, server_port = extract_hostname(request.decode('utf-8'))
    #print(f"Client is trying to connect to {hostname}")
    return hostname, server_port
    
def handle_CONNECT(client_socket, server_ip, server_port, hostname):
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    server_socket = ssl_context.wrap_socket(server_socket, server_hostname=hostname)   
    server_socket.connect((server_ip, 443))
    print(f"Connection established with the server at {server_ip}:{server_port}") 
    client_socket.send('HTTP/1.1 200 Connection Established\r\n\r\n'.encode())
    
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(proxy_certificate, proxy_private_key)
    client_socket = ssl_context.wrap_socket(client_socket, server_side=True)
    client_socket.do_handshake()
    return client_socket, server_socket
    

def proxying(client_socket, server_socket): #Forwards packets between client and the server
    	
    print("Starting proxy communication...")
    client_socket.settimeout(1)
    server_socket.settimeout(1)
    end_communication = 0
    while True:
        try:
            while True:
                request = client_socket.recv(1024)
                if url_filter.check_url(extract_url(request.decode('utf-8'))) == 0:
                    print(f"Client is trying to visit a blocked website!")
                    client_socket.send('HTTP/1.1 405 Requested website is blocked!\r\n\r\n'.encode())
                    end_communication = 1
                    break
                if not request: 
                    print("Client has received all of the requested files")
                    end_communication = 1
                    break
                print(f"REQUEST: \n\n{request}")
                server_socket.sendall(request)
                print("Request sent!")
        except socket.timeout:
            print("Client socket timed out!")
        if end_communication == 1:
            break
        try:
            while True:
                response = server_socket.recv(1024)
                if not response: break
                #print(f"RESPONSE: \n\n{response}")
                client_socket.sendall(response)
                #print("Response received!")
        except socket.timeout:
            print("Server socket timed out!")
    print("Communication complete!")
    client_socket.close()
    server_socket.close()
    



