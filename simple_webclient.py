import socket
import webbrowser
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('localhost', 9000))
cmd='GET http://localhost/page1.htm HTTP/1.0\r\n\r\n'.encode()
#cmd='GET http://localhost/index.htm HTTP/1.0\r\n\r\n'.encode()
#cmd='GET http://localhost/Hello+World.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
pieces=cmd.decode()
fname=""
for _ in pieces.split('/'):
    if "HTTP" in _:
        piece=_.split()
        piece=piece[0].split("+")
        for p in piece:
            fname+=p+" "
        fname=fname[:len(fname)-1]
fname+="l"
html=""
while True:
    data=mysock.recv(512)
    if len(data)<1:
        break
    html=data.decode()

mysock.close()

split_index=html.index("<")
html=html[split_index:len(html)-1]

f=open(fname,'w')
f.write(html)
f.close()
webbrowser.open_new_tab(fname)