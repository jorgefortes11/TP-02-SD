import socket
from controller import handle_request

HOST = '192.168.1.163'
PORT = 5003

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")  
    conn, addr = s.accept()
with conn:
    print(f"Conectado por {addr[0]}:{addr[1]}")
    while True:
        data = conn.recv(1024)
        if not data:
            print("Conexão encerrada pelo cliente.")
            break

        mensagem = data.decode()
        print(f"[RECEBIDO do cliente] {mensagem}")

        if mensagem == "EXIT":
            print("Cliente solicitou saída.")
            break

        resposta = handle_request(mensagem)
        print(f"[RESPOSTA enviada] {resposta}")
        conn.sendall(resposta.encode())
