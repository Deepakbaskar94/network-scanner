# Python3 code to display hostname and
# IP address

 
# Importing socket library
import socket
 
# Function to display hostname and
# IP address
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        #host_name = socket.getfqdn('192.168.1.1')
        #host_name = socket.gethostbyaddr('192.168.1.1')
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
    except:
        print("Unable to get Hostname and IP")
 
# Driver code
get_Host_name_IP() #Function call
 
#This code is contributed by "Sharad_Bhardwaj".