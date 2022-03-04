import socket
print('==> BY EDDY <==')
print()
oport = list()
i = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = input('target ')
def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False
for x in range(1, 600):
    if pscan(x):
        print('port is OPEN ' + str(x))
        oport.append(str(x))
    else:
        print('port is CLOSED ' + str(x))
print(oport)
s.close()
