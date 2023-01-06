from PoERobot import *
from spatialmath import SE3, Twist3
from numpy import pi
from roboticstoolbox import ET, Robot

link1 = PoERevolute([0, 0, 1], [0, 0, 0])
link2 = PoERevolute([0, 0, 1], [1, 0, 0])
TE0 = SE3.Tx(2)

poe = PoERobot([link1, link2], TE0)

print(poe.fkine([0, 0]))
print(poe.fkine([3, -2]))

e = ET.Rz() * ET.tx(1) * ET.Rz() * ET.tx(1)

er = Robot(e)
