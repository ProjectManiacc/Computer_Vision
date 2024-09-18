import json
import socket
from typing import Any
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

def process_and_send_results(test_results: list[dict[str, Any]], server_ip, server_port):
    direction_map = {
        'Left Arrow': "left", 
        'Right Arrow': "right", 
        'Up Arrow': "forward"
    }
    for listOfDict in test_results:
        for key, value in listOfDict.items():
            if key in direction_map:
                direction = direction_map[key]
                send_data_to_server({"direction": direction}, server_ip, server_port)        

