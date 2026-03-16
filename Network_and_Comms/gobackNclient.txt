import socket
import sys
import pickle
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(message)s', datefmt="%H:%M:%S")

class Packet:
    TYPE_DATA = 0
    TYPE_ACK = 1

    def __init__(self, seq_no, ptype=TYPE_DATA, data=''):
        self.seq_no = seq_no
        self.ptype = ptype
        self.data = data

    def is_corrupt(self):
        return False

    def __str__(self):
        return f"Packet(seq={self.seq_no}, type={self.ptype}, data='{self.data}')"

def send_packet(sock, packet):
    sock.sendall(pickle.dumps(packet))

def recv_packet(sock):
    try:
        data = sock.recv(4096)
        return pickle.loads(data)
    except:
        return None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(sys.argv[1]) if len(sys.argv) > 1 else 3300
sock.connect(('localhost', port))

expected_seq = 0
recvd_data = []

def to_network_layer(data):
    recvd_data.append(data)

while True:
    try:
        pack = recv_packet(sock)
        if not pack:
            continue

        if pack.seq_no == expected_seq and not pack.is_corrupt():
            to_network_layer(pack.data)
            logging.info('[RECV] : %s', pack)
            ack = Packet(expected_seq, ptype=Packet.TYPE_ACK)
            send_packet(sock, ack)
            logging.info('[ACK] : %d', expected_seq)
            expected_seq = (expected_seq + 1) % 8
        else:
            logging.info('[DROP] : Out-of-order or corrupt %s', pack)
            ack = Packet((expected_seq - 1) % 8, ptype=Packet.TYPE_ACK)
            send_packet(sock, ack)
    except (ConnectionResetError, KeyboardInterrupt):
        break

logging.info('Connection closed. Data received: %s', ''.join(recvd_data))
sock.close()
