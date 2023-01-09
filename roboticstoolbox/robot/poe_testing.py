from PoERobot import *
from spatialmath import SE3
from roboticstoolbox import ET, Robot

"""
# Book example
link1 = PoERevolute([0, 0, 1], [0, 0, 0])
link2 = PoERevolute([0, 0, 1], [1, 0, 0])
TE0 = SE3.Tx(2)

poe = PoERobot([link1, link2], TE0)
poe2ets = Robot(poe.ets())

q = [0, 0]
q = [2.5, -1.78]
print(poe.fkine(q))
print(poe2ets.fkine(q))
"""

link1 = PoERevolute([0, 0, 1], [0, 0, 0])
link2 = PoERevolute([0, 1, 0], [0, 0, 0.2])
link3 = PoEPrismatic([0, 1, 0])
#link3 = PoERevolute([0, 1, 0], [0, 0, 0.5])
link4 = PoERevolute([0, -1, 0], [0.2, 0, 0.5])
TE0 = SE3(np.array([[1, 0, 0, 0.3], [0, 0, -1, 0], [0, 1, 0, 0.5], [0, 0, 0, 1]]))

poe = PoERobot([link1, link2, link3, link4], TE0)
poe2ets = Robot(poe.ets())

q = [0, 0, 0, 0]
q = [3*np.pi/4, -np.pi/4, 0.3, -3*np.pi/4]
print(poe.fkine(q))
print(poe2ets.fkine(q))



#e = ET.Rz() * ET.tx(1) * ET.Rz() * ET.tx(1)
#er = Robot(e)