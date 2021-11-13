import eel
import socket
import pickle
import threading
import sys
import security
from security import dict

connected = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = ''
eel.init('templates')
code_port = ''


@eel.expose
def get_code(code, name):
    global code_port
    global host
    global port
    code_port = code
    try:
        host = code_port.split(':')[0]
        port = code_port.split(':')[1]
    except Exception as e:
        eel.error_msg('Enter a proper code, error: ' + str(e))
    s.connect((host, int(port)))
    code = s.recv(1024).decode('utf-8')
    decoded = security.dict.decode_str(code)
    s.send(decoded.encode('utf-8'))
    approval = s.recv(1024).decode('utf-8')
    if approval == 'Approved':
        s.send(name.encode('utf-8'))
        thread = threading.Thread(target=recv_msg, args=())
        thread.start()
        eel.start('chat.html', port=5010, close_callback=quit_room)
    else:
        print('Server has not authorized this client...try again')


@eel.expose
def send_msg(msg):
    s.send(msg.encode('utf-8'))


@eel.expose
def quit_room():
    global connected
    s.send(pickle.dumps({}))
    connected = False
    sys.exit()


def recv_msg():
    print('Connected Starting to receive messages')
    while connected:
        msg = s.recv(2048)
        print('message received')
        try:
            msg = pickle.loads(msg)
            print(msg)
            eel.display_msg(msg[0], msg[1])
        except:
            print(msg.decode('utf-8'))
            eel.display_msg('Server', msg.decode())


eel.start('main.html', port=5000)
