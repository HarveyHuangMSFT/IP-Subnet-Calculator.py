
import math
import ipaddress

while True:
    
    #validates the IP address that the user inputs
    def validateIP():
        global listIP
        global ip
        while True:
            ip = input("\nWhat's the IP? ")
            listIP = ip.split(".")
            if (ip.startswith("169.254.")):
                print("Invalid ip, please try again") #apipa IP is an invalid IP
            elif (len(listIP) == 4) and (ip != "127.0.0.1") and (listIP[1] <= "255") and (listIP[2] <= "255") and (listIP[3] <= "255"):
                print("Valid IP\n")
                break
            else:
                print("Invalid IP, please try again\n")
    validateIP()

    #validates the subnet mask the user inputs
    def validateMask():
        global list_subnets
        global subnet
        while True:
            subnet = input("What's the subnet mask? REMINDER: Must be in IP format: ")
            subnet_octets = ['0', '128', '192', '224', '240', '248', '252', '254', '255']
            list_subnets = subnet.split(".")
            if (len(list_subnets) == 4) and (list_subnets[0] == "255") and (list_subnets[1] in subnet_octets) and\
            (list_subnets[2] in subnet_octets) and (list_subnets[3] in subnet_octets) and (list_subnets[0] >= list_subnets[1] >= list_subnets[2] >= list_subnets[3]):
                 print("Valid Subnet Mask\n")
                 break
            else:
                print("Invalid Subnet Mask, please try again")
    validateMask()

    def calculate():
        
            network_add = ipaddress.IPv4Network(ip + '/' + subnet, False)
            print("The network address is: " + str(network_add))
    
            list_hosts = list(network_add.hosts())
            print("Available Hosts: ", len(list_hosts))

            first_host = list(network_add.hosts())[0]
            last_host_position = len(list(network_add.hosts())) - 1
            last_host = list(network_add.hosts())[last_host_position]
            print("The host address range is: ", first_host, "-" ,last_host)

    calculate()

