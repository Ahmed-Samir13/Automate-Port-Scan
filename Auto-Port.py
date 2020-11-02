import socket

target = input("Enter the IP address: ")
portrange = input("Enter the port range (ex 10-500): ")

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print("Scanning host", target , "from port", lowport , "to port" , highport)

for port in range(lowport , highport):
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    status = s.connect_ex((target , port))
    if(status ==0):
        print("*** Port" , port , "Open ***")
    else:
        print("Port" , port , "- Close")
        s.close()
