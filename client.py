import socket
import os

PORT = 5001
client = None


logFile = None

def connect(ip):
    global client

    print("Connect to", ip)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, PORT))

def autoconnect():
    s = os.popen("ip route").read()
    ip = s.split("src")[-1].strip()

    connect(ip)

def record():
    logFile = open("log.dat", "wb")


def send_entry(entry):
    global client

    if logFile:
        logFile.write(entry.serializeToBinary())

    if client:
        client.send(entry.serializeToBinary())
