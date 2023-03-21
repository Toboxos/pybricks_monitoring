Example PyBricks file:

```python
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
#                                  InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks_monitoring.devices import (Motor, TouchSensor, ColorSensor,
                                  InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Connect to PC to stream data
connect("169.254.222.231")


# Use the sensors like you would with pybricks
sensor = UltrasonicSensor(Port.S4)
while True:
    distance = sensor.distance()
    print(distance)
```


Example Server file:
```python
#!/usr/bin/env python3
from pybricks_monitoring.server import *
server = Server('0.0.0.0', 5001, handle_client)
server.start()

```