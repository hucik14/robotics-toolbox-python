from roboticstoolbox import ERobot, ET
from spatialmath import SE3
from roboticstoolbox.models.ETS import Panda, Puma560


r = ERobot(ET.Rz() * ET.tx(1) * ET.tz(2) * ET.Rz() * ET.tx(1))
q = [3, -2]


p = Panda()
p.generate_URDF()
q = [0, 0, 0, 0, 0, 0, 0]
print(p.fkine(q))


# Init joint to the 'ready' joint angles
p.q = p.qr

# Open a plot with the teach panel
e = p.teach()