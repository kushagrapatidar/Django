from socket import *
def create_server():
    serversocket=socket(AF_INET,SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while 1:
            (clientsocket, address)=serversocket.accept()
            rd=clientsocket.recv(5000).decode()
            pieces=rd.split("\n")
            
            if len(pieces)>0 : print(pieces[0])
            fname=""
            for _ in pieces[0].split('/'):
                if "HTTP" in _:
                    piece=_.split()
                    piece=piece[0].split("+")
                    for p in piece:
                        fname+=p+" "
                    fname=fname[:len(fname)-1]
            fname+="l"
            f=open(fname,'r')
            html=f.read()
            data = "HTTP/1.1 200 OK\r\n"
            data+="Content-Type: text/html; charset-utf-8\r\n"
            data+="\r\n"
            data+=html
            data+="\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)


    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
create_server()