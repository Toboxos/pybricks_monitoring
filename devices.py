import time

import pybricks.ev3devices as ev3
from pybricks.parameters import Port
from .data import Entry, SensorType, DataType
from .client import send_entry

# ev3 port to port number
def getPortNumber(port):
    if port == Port.S1:
        return 1
    elif port == Port.S2:
        return 2
    elif port == Port.S3:
        return 3
    elif port == Port.S4:
        return 4
    elif port == Port.A:
        return 5
    elif port == Port.B:
        return 6
    elif port == Port.C:
        return 7
    elif port == Port.D:
        return 8
    else:
        return 0


class UltrasonicSensor(ev3.UltrasonicSensor):
    def __init__(self, port):
        super().__init__(port)
        self.port = getPortNumber(port)

    def distance(self):
        value = super().distance()

        entry = Entry(int(time.time() * 1000), SensorType.ULTRASONIC, self.port, DataType.DISTANCE, value)
        send_entry(entry)

        return value

class TouchSensor(ev3.TouchSensor):
    def __init__(self, port):
        super().__init__(port)
        self.port = getPortNumber(port)

    def pressed(self):
        value = super().pressed()

        entry = Entry(int(time.time() * 1000), SensorType.TOUCH, self.port, DataType.BOOL, value)
        send_entry(entry)

        return value

class ColorSensor(ev3.ColorSensor):
    def __init__(self, port):
        super().__init__(port)
        self.port = getPortNumber(port)

    def color(self):
        value = super().color()

        entry = Entry(int(time.time() * 1000), SensorType.COLOR, self.port, DataType.COLOR, value)
        send_entry(entry)

        return value

    def ambient(self):
        value = super().ambient()

        entry = Entry(int(time.time() * 1000), SensorType.COLOR, self.port, DataType.AMBIENT, value)
        send_entry(entry)

        return value

    def reflection(self):
        value = super().reflection()

        entry = Entry(int(time.time() * 1000), SensorType.COLOR, self.port, DataType.REFLECTION, value)
        send_entry(entry)

        return value

class InfraredSensor(ev3.InfraredSensor):
    def __init__(self, port):
        super().__init__(port)
        self.port = getPortNumber(port)

    def distance(self):
        value = super().distance()

        entry = Entry(int(time.time() * 1000), SensorType.INFRARED, self.port, DataType.PERCENT, value)
        send_entry(entry)

        return value

class GyroSensor(ev3.GyroSensor):
    def __init__(self, port):
        super().__init__(port)
        self.port = getPortNumber(port)

    def angle(self):
        value = super().angle()

        entry = Entry(int(time.time() * 1000), SensorType.GYRO, self.port, DataType.DISTANCE, value)
        send_entry(entry)

        return value

    def speed(self):
        value = super().speed()

        entry = Entry(int(time.time() * 1000), SensorType.GYRO, self.port, DataType.SPEED, value)
        send_entry(entry)

        return value