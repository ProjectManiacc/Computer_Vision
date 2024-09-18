import json
import logging
from dataclasses import dataclass
from socket import socket, AF_INET, SOCK_STREAM

Logger = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.INFO)

HostIp: str = "localhost"
HostPort: int = 8080


@dataclass
class AgvCommand:
    left_wheel: bool = False
    right_wheel: bool = False


def sendAgvCommand(command: AgvCommand):
    BoolToStr = ("OFF", "ON")
    Logger.info(f"Left engine: {BoolToStr[command.left_wheel]}")
    Logger.info(f"Right engine: {BoolToStr[command.right_wheel]}")
    # Set the appropriate GPIO pins high/low to change the engines' state using the PLC
    pass


DirectionToCommand: dict[str, AgvCommand] = {
    "left": AgvCommand(left_wheel=False, right_wheel=True),
    "right": AgvCommand(left_wheel=True, right_wheel=False),
    "forward": AgvCommand(left_wheel=True, right_wheel=True),
    "stop": AgvCommand(left_wheel=False, right_wheel=False),
}


def processLoop(s: socket):
    while True:
        s.listen(1)
        connection, client_address = s.accept()
        data = connection.recv(1024)
        Logger.debug(f"Received {len(data)} bytes from {client_address}")

        try:
            result = json.loads(data.decode())
        except json.JSONDecodeError:
            Logger.warning(f'Skipping invalid JSON: "{data.decode()}"')
            continue

        direction = result.get("direction")
        command = DirectionToCommand.get(direction)
        if command is None:
            Logger.warning(f'Skipping invalid direction: "{direction}"')
            continue

        Logger.info(f'Received command "{direction}"')
        sendAgvCommand(command)


def main():
    Logger.info("Starting AGV Command Receiver")

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((HostIp, HostPort))
        Logger.info(f"Opened a TCP socket at {HostIp}:{HostPort}")
        processLoop(s)


if __name__ == "__main__":
    main()
