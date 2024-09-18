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
        print(f"Wysłano dane: {json_data}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")

    finally:
        client_socket.close()
        print(f"Zamknięto socket")


def process_and_send_results(test_results: list[dict[str, Any]], server_ip, server_port):
    direction_map = {
        'Left Arrow': "left",
        'Right Arrow': "right",
        'Up Arrow': "forward"
    }
    for listOfDict in test_results:
        for key, value in listOfDict.items():

            if value['label'] in direction_map:
                print(f"Odnaleziono obiekt: {value['label']}")
                direction = direction_map[key]
                data = {"direction": direction}
                print(f"Przesyłane dane: {data}")
                send_data_to_server(data, server_ip, server_port)