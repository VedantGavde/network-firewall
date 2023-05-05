import socket
import ipaddress

# The function below asks the admin user to add or remove source ports to/from the file called src_ports.txt
def add_remove_src_ports(): 
    print("The source ports are listed below:")
    file = open("src_ports.txt","r")
    for line in file:
        print(line.strip()) #Display all the ports in the file
    while (1):
        response = input("Do you want to add or remove source ports from this list:\nPress 1 for Add \nPress 2 for Remove\nPress 3 to Skip\n")
        if response == '1':
            while(1):
                try:
                    get_port = int(input("Enter the port number to be added to the list:\n"))
                except:
                    print("Can only enter numbers between 0 to 65535") #Checking for valid input values
                else:
                    if get_port < 0 or get_port > 65535: #0 to 65535 
                        print("Invalid Port\nPlease enter a valid choice") #Checking if the entry is within the valid range of ports
                    else:
                        file = open("src_ports.txt","r")
                        flag = 0
                        for line in file:
                            if int(line.strip())==get_port: #Check if the port already exists in the file
                                print("The port number already exists") 
                                flag = 1
                                break
                        if flag == 0: #Add the port to the file
                            file = open("src_ports.txt","a")
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
                    print("Can only enter numbers between 0 to 65535") #Checking for valid input values
                else:
                    if get_port < 0 or get_port > 65535: #0 to 65535
                        print("Invalid Port\nPlease enter a valid choice") #Checking if the entry is within the valid range of ports
                    else:
                        file = open("src_ports.txt","r")
                        data = file.readlines()
                        file = open("src_ports.txt","w")
                        flag = 0
                        for line in data:
                            if line.strip()!=str(get_port): #Add the port to the file only if it doesn't match the port number that is to be removed
                                file.write(line)
                        break
            break
        elif response == '3':
            break
        else:
            print("Invalid choice\nPlease enter a valid choice")
    return


# The function below asks the admin user to add or remove destination ports to/from the file called dst_ports.txt    
def add_remove_dst_ports():
    print("The destination ports are listed below:")
    file = open("dst_ports.txt","r")
    for line in file:
        print(line.strip()) #Display all the ports in the file
    while (1):
        response = input("Do you want to add or remove destination ports from this list:\nPress 1 for Add \nPress 2 for Remove\nPress 3 to Skip\n")
        if response == '1':
            while(1):
                try:
                    get_port = int(input("Enter the port number to be added to the list:\n"))
                except:
                    print("Can only enter numbers between 0 to 65535")#Checking for valid input values
                else:
                    if get_port < 0 or get_port > 65535: #0 to 65535
                        print("Invalid Port\nPlease enter a valid choice") #Checking if the entry is within the valid range of ports
                    else:
                        file = open("dst_ports.txt","r")
                        flag = 0
                        for line in file:
                            if int(line.strip())==get_port:
                                print("The port number already exists")
                                flag = 1
                                break
                        if flag == 0: #Add the port to the file
                            file = open("dst_ports.txt","a")
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
                    print("Can only enter numbers between 0 to 65535") #Checking for valid input values
                else:
                    if get_port < 0 or get_port > 65535: #0 to 65535
                        print("Invalid Port\nPlease enter a valid choice") #Checking if the entry is within the valid range of ports
                    else:
                        file = open("dst_ports.txt","r")
                        data = file.readlines()
                        file = open("dst_ports.txt","w")
                        flag = 0
                        for line in data:
                            if line.strip()!=str(get_port): #Add the port to the file only if it doesn't match the port number that is to be removed
                                file.write(line)
                        break
            break
        elif response == '3':
            break
        else:
            print("Invalid choice\nPlease enter a valid choice")
    return


# The function below asks the admin user to add or source IP addresses to/from the file called src_ip.txt        
def add_remove_src_ips():
    print("The Source IPs are listed below:")
    file = open("src_ip.txt","r")
    for line in file:
        print(line.strip()) #Display all the IP addresses in the file
    while (1):
        response = input("Do you want to add or remove IP address from this list:\nPress 1 for Add \nPress 2 for Remove\nPress 3 to Skip\n")
        if response == '1':
            while(1):
                ip_address = input("Enter IP address: ")
                try:
                    socket.inet_aton(ip_address) #Checking to see if the IP entered is valid or not
                except socket.error:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                try:
                     ipaddress.ip_address(ip_address) #Checking to see if the IP entered is valid or not
                except ValueError:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                else:
                    file = open("src_ip.txt","a")
                    file.write(ip_address + "\n") #Add IP to the file
                    break
            break
        elif response == '2':
            while(1):
                ip_address = input("Enter IP address: ")
                try:
                    socket.inet_aton(ip_address) #Checking to see if the IP entered is valid or not
                except socket.error:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                try:
                     ipaddress.ip_address(ip_address) #Checking to see if the IP entered is valid or not
                except ValueError:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                else:
                    file = open("src_ip.txt","r")
                    data = file.readlines()
                    file = open("src_ip.txt","w")
                    flag = 0
                    for line in data:
                        if line.strip()!=ip_address: #Add IP to the file only if it doesn't match the IP to be removed
                            file.write(line)
                    print("before break")
                    break
            break
        elif response == '3':
            break
        else:
           print("Invalid choice\nPlease enter a valid choice")
    return


# The function below asks the admin user to add or destination IP addresses to/from the file called dst_ip.txt
def add_remove_dst_ips():
    print("The Destination IPs are listed below:")
    file = open("dst_ip.txt","r")
    for line in file:
        print(line.strip()) #Display all the IP addresses in the file
    while (1):
        response = input("Do you want to add or remove IP address from this list:\nPress 1 for Add \nPress 2 for Remove\nPress 3 to Skip\n")
        if response == '1':
            while(1):
                ip_address = input("Enter IP address: ")
                try:
                    socket.inet_aton(ip_address) #Checking to see if the IP entered is valid or not
                except socket.error:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                try:
                     ipaddress.ip_address(ip_address) #Checking to see if the IP entered is valid or not
                except ValueError:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                else:
                    file = open("dst_ip.txt","a")
                    file.write(ip_address + "\n") #Add IP to the file
                    break
            break
        elif response == '2':
            while(1):
                ip_address = input("Enter IP address: ")
                try:
                    socket.inet_aton(ip_address) #Checking to see if the IP entered is valid or not
                except socket.error:
                    print("Invalid IP address\nPlease Enter a vild IP address")
                try:
                     ipaddress.ip_address(ip_address) #Checking to see if the IP entered is valid or not
                except ValueError: 
                    print("Invalid IP address\nPlease Enter a vild IP address")
                else:
                    file = open("dst_ip.txt","r")
                    data = file.readlines()
                    file = open("dst_ip.txt","w")
                    flag = 0
                    for line in data:
                        if line.strip()!=ip_address: #Add IP to the file only if it doesn't match the IP to be removed
                            file.write(line) 
                    print("before break")
                    break
            break
        elif response == '3':
            break
        else:
           print("Invalid choice\nPlease enter a valid choice")
    return

        
# The function below returns 0 or 1 based on the values of the source IP and port. If 0 is returned then the calling function drops the packet else accpets it        
def block_src_packets(src, prt):
    file = open("src_ip.txt","r")
    src_ips = file.readlines()
    src_ips = [i.strip() for i in src_ips]
    file = open("src_ports.txt","r")
    ports = file.readlines()
    ports = [i.strip() for i in ports]
    if src in src_ips: #Check if the source IP is in the list of allowed source IPS
        if (prt not in ports):#Check if the port is not in the list of blocked source IPS
            print("Letting it through")
            return 1
        else:
            print("The source port has been blocked for use. Dropping this one")
            return 0
    else:
        print("Dropping this one")
        return 0
       
# The function below returns 0 or 1 based on the values of the destination IP and port. If 0 is returned then the calling function drops the packet else accpets it
def block_dst_packets(dst, prt):
    file = open("dst_ip.txt","r")
    dst_ips = file.readlines()
    dst_ips = [i.strip() for i in dst_ips]
    file = open("dst_ports.txt","r")
    ports = file.readlines()
    ports = [i.strip() for i in ports]
    if dst not in dst_ips: #Check if the destincation IP is in the list of allowed destination IPS
        if (prt not in ports):#Check if the port is not in the list of blocked source IPS
            print("Letting it through")
            return 1
        else:
            print("The Destination port has been blocked for use. Dropping this one")
            return 0
    else:
        print("Dropping this one")
        return 0
