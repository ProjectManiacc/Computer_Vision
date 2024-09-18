import json
import logging
import random
from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

Logger = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.INFO)

Directions = ("left", "right", "forward", "stop", "garbage", 123, None)

HostIp = "localhost"
HostPort = 8080


def sendData(s: socket):
    choice = random.choice(Directions)
    command = json.dumps({"direction": choice})
    s.sendall(command.encode())
    s.close()
    Logger.info(f'Sent "{choice}" command')


def main():
    Logger.info("Starting AGV Command Sender")
    Logger.info(f"Sending data to host {HostIp}:{HostPort}")
    while True:
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((HostIp, HostPort))
            sendData(s)
        sleep(1)


if __name__ == "__main__":
    main()
