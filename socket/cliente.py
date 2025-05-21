import socket

HOST = '192.168.1.163'
PORT = 5002

def menu():
    print("\n1. Add Task")      
    print("2. List Tasks")      
    print("3. Remove Task")      
    print("0. Exit")        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        menu()
        option = input("Choose: ")
        if option == '1':
            task = input("Enter task description: ")
            s.sendall(f"ADD {task}".encode())
        elif option == '2':
            s.sendall("LIST".encode())
        elif option == '3':
            task_id = input("Enter task ID to remove: ")
            s.sendall(f"REMOVE {task_id}".encode())
        elif option == '0':
            s.sendall("EXIT".encode())
            break
        else:
            print("Invalid option.")
            continue
        response = s.recv(1024)
        print("Response:", response.decode())
