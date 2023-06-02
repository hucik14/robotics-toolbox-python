from roboticstoolbox import ERobot, ET
from roboticstoolbox.models.ETS import Panda


r = ET.Rz() * ET.tz(0.2) * ET.Rz(-1.5707963267948966) * ET.Ry(-1.5707963267948966) * ET.Rz() * ET.tz() * ET.tx(0.3) * ET.ty(0.2) * ET.Rz(0.5880026035475676) * ET.Rx(3.141592653589793) *  ET.Rz() * ET.tx(0.05547001962252285) * ET.ty(-0.08320502943378433) * ET.Rz(eta=-0.9827937232473289)
r = ERobot(r)
r.generate_URDF()

p = Panda()
p.generate_URDF('mypanda.urdf')

