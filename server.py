#!/usr/bin/env python3
import socket
import struct
import threading

from .data import Entry, SensorType, DataType

class Server:
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)

    def start(self):
        print("Listening...")
        while True:
            connection, address = self.socket.accept()
            print(f"New connection '{address}'")
            threading.Thread(target=self.handler, args=(connection, address)).start()


def handle_client(client, address):
    while True:
        data = client.recv(struct.calcsize(Entry.FORMAT_STRING))
        if len(data) == 0:
            break

        entry = Entry(0, 0, 0, 0, 0)
        entry.deserializeFromBinary(data)

        # Print entry
        print(f"[{entry.timestamp}] SensorType={entry.sensorType} SensorPort{entry.sensorPort} valueType={entry.valueType} value={entry.value}")

if __name__ == '__main__':
    server = Server('0.0.0.0', 5001, handle_client)
