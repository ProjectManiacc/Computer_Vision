import socket

def send_data_to_server(data, server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))        
        client_socket.sendall(data.encode('utf-8'))
        response = client_socket.recv(1024)
        print(f"Otrzymano odpowiedź: {response.decode('utf-8')}")
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    
    finally:
        client_socket.close()

