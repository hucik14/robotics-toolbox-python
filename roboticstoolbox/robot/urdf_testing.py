from roboticstoolbox import ERobot, ET
from spatialmath import SE3
from roboticstoolbox.models.ETS import Panda, Puma560
import numpy as np

r = ERobot(ET.Rz() * ET.tx(1) * ET.tz(2) * ET.Rz() * ET.tx(1))
q = [3, -2]

r = ET.Rz() * ET.tz(0.2) * ET.Rz(-1.5707963267948966) * ET.Ry(-1.5707963267948966) * ET.Rz() * ET.tz() * ET.tx(0.3) * ET.ty(0.2) * ET.Rz(0.5880026035475676) * ET.Rx(3.141592653589793) *  ET.Rz() * ET.tx(0.05547001962252285) * ET.ty(-0.08320502943378433) * ET.Rz(eta=-0.9827937232473289)
r = ERobot(r)

r.generate_URDF('rob.urdf')

q = [np.pi/7, -np.pi/5, 0.3, -np.pi/3]

"""
p = Panda()
p.generate_URDF()
q = [0, 0, 0, 0, 0, 0, 0]
print(p.fkine(q))


# Init joint to the 'ready' joint angles
p.q = p.qr

# Open a plot with the teach panel
e = p.teach()

"""
