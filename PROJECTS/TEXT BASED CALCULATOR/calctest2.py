import math
import numpy as np
from numpy import cos, degrees, radians
x = 45
x_rad = math.cos(math.degrees(math.radians((x))))
#cosValue = math.cos(x_rad)
#cosConvert = math.degrees(cosValue)
#print(f"{round(cosValue,2)} radians")
#print(f"{round(cosConvert,2)} degrees")
print(f"{x_rad:.2}")
