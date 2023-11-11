import socket
#client dont't wait other clients sperate code
import threading

HEADER =64
PORT = 5050
#SERVER = "192.168.1.33"#ipconfig IPV4
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MSG ="DISCONNECT"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)

#Fonk for handle spreaded threads
def handle_client(conn,addr):#connection,addres
    print(f"[NEW CONNECTİON] {addr} connected")
    connected = True

    while connected:
        #İstemciden ilk olarak ileti başlığını alır (ne kadar veri alınacağını belirler) ve ardından gerçek iletiyi alır.
        #Eğer ileti DISCONNECT_MSG ile aynı ise, bağlantıyı sonlandırır.
        msg_lenght= conn.recv(HEADER).decode(FORMAT) #receive how many byte
        if msg_lenght:#TEST msg comes
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr} {msg}]")
            conn.send("Msg received".encode(FORMAT))#msg from server
    conn.close()


def start():
    server.listen()
    print(f"[LİSTENİNG] server {SERVER}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTİONS] {threading.active_count() - 1}")






print("[STARTİNG]...")
start()

