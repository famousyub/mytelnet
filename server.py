import socket

def server():
    TCP_IP = "192.168.5.1"
    TCP_PORT = 8000
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('TCP_IP', TCP_PORT))
    s.listen(1)
    
    conn, addr = s.accept()
    print ('Connection address:', addr)
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print ("received data:", data)
        conn.send(data)  # echo
    conn.close()
    
server()