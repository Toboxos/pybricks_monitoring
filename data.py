import struct

class Entry:
    FORMAT_STRING = '!QBBBi'

    def __init__(self, timestamp, sensorType, sensorPort, valueType, value):
        self.timestamp = timestamp
        self.sensorType = sensorType
        self.sensorPort = sensorPort
        self.valueType = valueType
        self.value = value

    def serializeToBinary(self):
        return struct.pack(Entry.FORMAT_STRING, self.timestamp, self.sensorType, self.sensorPort, self.valueType, self.value)

    def deserializeFromBinary(self, data):
        self.timestamp, self.sensorType, self.sensorPort, self.valueType, self.value = struct.unpack(Entry.FORMAT_STRING, data)

# SensorType Enum
class SensorType:
    TOUCH = 0
    COLOR = 1
    ULTRASONIC = 2
    GYRO = 3
    INFRARED = 4
    MOTOR = 5


# Data Type
class DataType():
    DISTANCE = 0
    COLOR = 1
    AMBIENT = 2
    REFLECTION = 3
    BOOL = 4
    PERCENT = 5
    ANGLE = 6
    SPEED = 7
