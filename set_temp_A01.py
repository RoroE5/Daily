import maya.cmds as mc

sels = mc.ls(sl=True)

# for jnt in sels:
#     jntrz = mc.getAttr("%s.rz"%jnt)
#     if jntrz > 60:
#         newjntrz = jntrz-180
#         mc.setAttr("%s.rz"%jnt,newjntrz)
#     elif jntrz < -120:
#         newjntrz = jntrz+180
#         mc.setAttr("%s.rz"%jnt,newjntrz)
    
#     jntry = mc.getAttr("%s.ry"%jnt)
#     if jntry > 100:
#         newjntry = (jntry-180)*-1
#         mc.setAttr("%s.ry"%jnt,newjntry)
#     elif jntry < -100:
#         newjntry = (jntry+180)*-1
#         mc.setAttr("%s.ry"%jnt,newjntry)
    
#     jntrx = mc.getAttr("%s.rx"%jnt)
#     if jntrx > 100:
#         newjntrx = jntrx-180
#         mc.setAttr("%s.rx"%jnt,newjntrx)
#     elif jntrx < -100:
#         newjntrx = jntrx+180
#         mc.setAttr("%s.rx"%jnt,newjntrx)
t=1
while (t):
    mc.currentTime(t)
    t = t+1
    if t==14:
        break
    else:
        for jnt in sels:
            jntrz = mc.getAttr("%s.rz"%jnt)
            if jntrz > 60:
                newjntrz = jntrz-180
                mc.setAttr("%s.rz"%jnt,newjntrz)
            elif jntrz < -120:
                newjntrz = jntrz+180
                mc.setAttr("%s.rz"%jnt,newjntrz)
            
            jntry = mc.getAttr("%s.ry"%jnt)
            if jntry > 100:
                newjntry = (jntry-180)*-1
                mc.setAttr("%s.ry"%jnt,newjntry)
            elif jntry < -100:
                newjntry = (jntry+180)*-1
                mc.setAttr("%s.ry"%jnt,newjntry)
            
            jntrx = mc.getAttr("%s.rx"%jnt)
            if jntrx > 100:
                newjntrx = jntrx-180
                mc.setAttr("%s.rx"%jnt,newjntrx)
            elif jntrx < -100:
                newjntrx = jntrx+180
                mc.setAttr("%s.rx"%jnt,newjntrx)
    
            
