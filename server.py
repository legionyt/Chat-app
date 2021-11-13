import socket
import threading
import pickle
from pyngrok import ngrok
import security
from security import dict

host = '127.0.0.1'
port = 5050
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
clients = {}


def broadcast(msg, is_text):
    print(f'Broadcasting message {str(msg)}')
    for i in clients:
        if is_text:
            print(f'Broadcasting message to {i}')
            clients[i].send(msg.encode('utf-8'))
        elif not is_text:
            print(f'Broadcasting message to {i}')
            clients[i].send(pickle.dumps(msg))


def handle_client(conn, addr):
    random_str = security.dict.random_str()
    print(f'New connection attempt from {str(addr)}')
    print(f'Authorizing...')
    conn.send(security.dict.encode_str(random_str).encode('utf-8'))
    code = conn.recv(1024).decode('utf-8')
    if code == random_str:
        conn.send('Approved'.encode('utf-8'))
        print('Authorized')
        name = conn.recv(2048).decode('utf-8')
        clients[name] = conn
        broadcast(f'Welcome {name} to the server', True)
        while True:
            msg = conn.recv(2048)
            try:
                msg = pickle.loads(msg)
                print(f'{list(clients.keys())[list(clients.values()).index(conn)]} has disconnected')
                broadcast(f'{list(clients.keys())[list(clients.values()).index(conn)]} has disconnected', True)
                break
            except:
                msg = msg.decode('utf-8')
                broadcast([list(clients.keys())[list(clients.values()).index(conn)], msg], False)
                print(f'[{list(clients.keys())[list(clients.values()).index(conn)]}]: {msg}')
    else:
        print(f'{str(addr)} has not been authorized')
        print(f'Authcode {random_str} has not matched with return value {code}')


print('Server is listening...')
s.listen()
ngrok.set_auth_token('1oKXCEyBJBZzLjaxlScfawQsFBH_HeUsFkWjrcUMUYWpzfHS')
url = ngrok.connect(port, proto='tcp').public_url
ip_port = url.strip('tcp://')
print(f'Ngrok address {url}')
address = ip_port.split(':')
print(f'Ngrok Address: {address}')
print(f"Length of IP: {len(ip_port.strip(ip_port.split(':')[1]).strip(':'))}")
ip = socket.gethostbyname(address[0])
print(f'IP of ngrok tunnel: {ip}')
print(f'Code: {ip + ":" + ip_port.split(":")[1]}')
while True:
    conn, addr = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()