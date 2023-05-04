import firewall
import proxy
import url_filter
import socket
import ssl

buffer_size = 4096
listener_port = 8080
port_server = 443
proxy_certificate = './../certificate.crt'  
proxy_private_key = './../private.key'

listener_socket = proxy.setup_listener(listener_port, proxy_certificate, proxy_private_key)

while True:
    
    client_socket, client_address = proxy.receive_connection(listener_socket)
    
    if firewall.block_packets(client_address[0], client_address[1], 0) == 0: #client_address[0] is source IP and client_address[1] is source port
        client_socket.send('HTTP/1.1 403 Client device is blocked on the firewall\r\n\r\n'.encode())
        client_socket.close()
        continue
    
    hostname, destination_port = proxy.get_hostname(client_socket)
    #Can check blacklisted domains here
    try:
        server_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f"Failed to resolve the domain : {hostname}")
        return 0
    if firewall.block_packets(server_ip, destination_port, 1) == 0:
        client_socket.send('HTTP/1.1 405 Destination server is blocked on the firewall\r\n\r\n'.encode())
        client_socket.close()
        continue
        
    client_socket, server_socket = proxy.handle_CONNECT(client_socket, server_ip, destination_port)
    proxy.proxying(client_socket, server_socket)
