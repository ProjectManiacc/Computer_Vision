import json
import socket
from urllib import response

def send_data_to_server(data, server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))      
        json_data = json.dumps(data)  
        client_socket.sendall(json_data.encode('utf-8'))
        print(f"Otrzymano odpowiedź: {response.decode('utf-8')}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    
    finally:
        client_socket.close()

        

