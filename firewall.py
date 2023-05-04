from netfilterqueue import NetfilterQueue
from scapy.all import *
import socket
import ipaddress

def add_remove_ports():
    print("The ports are listed below:")
    file = open("ports.txt","r")
    for line in file:
        print(line.strip())
    while (1):
        response = input("Do you want to add or remove ports from this list:\nPress 1 for Add \nPress 2 for Remove\nPress 3 to Skip\n")
        if response == '1':
            while(1):
                try:
                    get_port = int(input("Enter the port number to be added to the list:\n"))
                except:
                    print("Can only enter numbers between 0 to 65535")
                else:
                    if get_port < 0 or get_port > 65535: #0 to 65535
                        print("Invalid Port\nPlease enter a valid choice")
                    else:
                        file = open("ports.txt","r")
                        flag = 0
                        for line in file:
                            if int(line.strip())==get_port:
                                print("The port number already exists")
                                flag = 1
                                break
                        if flag == 0:
                            file = open("ports.txt","a")
                            file.write(str(get_port) + "\n")
                            break
                        else:
                            break
            break
        elif response == '2':
            while(1):
                try:
                    get_port = int(input("Enter the port number to be removed to the list:\n"))
                except:
                    print("Can only enter numbers between 0 to 65535")
                else:
                    if get_port < 0 or get_port > 65535: #0 to 65535
                        print("Invalid Port\nPlease enter a valid choice")
                    else:
                        file = open("ports.txt","r")
                        data = file.readlines()
                        file = open("ports.txt","w")
                        flag = 0
                        for line in data:
                            if line.strip()!=str(get_port):
                                file.write(line)
                        break
            break
        elif response == '3':
            break
        else:
            print("Invalid choice\nPlease enter a valid choice")
    return
def add_remove_src_ips():
    print("The Source IPs are listed below:")
    file = open("src_ip.txt","r")
    for line in file:
        print(line.strip())
    while (1):
        response = input("Do you want to add or remove IP address from this list:\nPress 1 for Add \nPress 2 for Remove\nPress 3 to Skip\n")
        if response == '1':
            while(1):
                ip_address = input("Enter IP address: ")
                try:
                    socket.inet_aton(ip_address)
                except socket.error:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                try:
                     ipaddress.ip_address(ip_address)
                except ValueError:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                else:
                    file = open("src_ip.txt","a")
                    file.write(ip_address + "\n")
                    break
            break
        elif response == '2':
            while(1):
                ip_address = input("Enter IP address: ")
                try:
                    socket.inet_aton(ip_address)
                except socket.error:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                try:
                     ipaddress.ip_address(ip_address)
                except ValueError:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                else:
                    file = open("src_ip.txt","r")
                    data = file.readlines()
                    file = open("src_ip.txt","w")
                    flag = 0
                    for line in data:
                        if line.strip()!=ip_address:
                            file.write(line)
                    print("before break")
                    break
            break
        elif response == '3':
            break
        else:
           print("Invalid choice\nPlease enter a valid choice")
    return
def add_remove_dst_ips():
    print("The Destination IPs are listed below:")
    file = open("dst_ip.txt","r")
    for line in file:
        print(line.strip())
    while (1):
        response = input("Do you want to add or remove IP address from this list:\nPress 1 for Add \nPress 2 for Remove\nPress 3 to Skip\n")
        if response == '1':
            while(1):
                ip_address = input("Enter IP address: ")
                try:
                    socket.inet_aton(ip_address)
                except socket.error:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                try:
                     ipaddress.ip_address(ip_address)
                except ValueError:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                else:
                    file = open("dst_ip.txt","a")
                    file.write(ip_address + "\n")
                    break
            break
        elif response == '2':
            while(1):
                ip_address = input("Enter IP address: ")
                try:
                    socket.inet_aton(ip_address)
                except socket.error:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                try:
                     ipaddress.ip_address(ip_address)
                except ValueError:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                else:
                    file = open("dst_ip.txt","r")
                    data = file.readlines()
                    file = open("dst_ip.txt","w")
                    flag = 0
                    for line in data:
                        if line.strip()!=ip_address:
                            file.write(line)
                    print("before break")
                    break
            break
        elif response == '3':
            break
        else:
           print("Invalid choice\nPlease enter a valid choice")
    return


def block_packets(src, dest, prt):
    file = open("src_ip.txt","r")
    src_ips = file.readlines()
    src_ips = [i.strip() for i in src_ips]
    file = open("dst_ip.txt","r")
    dst_ips = file.readlines()
    dst_ips = [i.strip() for i in dst_ips]
    file = open("ports.txt","r")
    ports = file.readlines()
    if (src in src_ips):
        if(dest not in dst_ips):
            try:
                if (prt not in ports):
                    pkt.accept()
                    print("letting it through")
                    return 1
                else:
                    print("The destination port has been blocked for use. Dropping this one")
                    return 0
            except AttributeError:
                print("dropping this one due to port error")
                return 0
        else:
            print("The destination IP has been blocked for use. Dropping this one")
            return 0
    else:
        print("dropping this one")
        return 0
        
