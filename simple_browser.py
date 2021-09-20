import socket
import webbrowser
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd='GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

html=""
while True:
    data=mysock.recv(512)
    if len(data)<1:
        break
    html=data.decode()

mysock.close()

split_index=html.index("<")
html=html[split_index:len(html)-1]

fname="page1.html"
page1=open(fname,'w')
page1.write(html)
page1.close()
webbrowser.open_new_tab(fname)