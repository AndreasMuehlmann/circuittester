import serial
import time


class SerialConnection:
    def __init__(self, port: str):
        self.connection = serial.Serial(port, 9600, timeout=1.0)
        time.sleep(0.5)

    def recv(self):
        return self.connection.readline().decode().strip()

    def send(self, data):
        self.connection.write(str(data).encode() + b'\n')

    def reset(self):
        self.connection.close()
