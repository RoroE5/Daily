import maya.cmds as mc

sels = ['Note_1_C1_ctl', 'Note_1_C2_ctl', 'Note_1_C3_ctl', 'Note_1_C4_ctl'] #选择每个音符的主控制器
mc.select(cl=1)
for rootctrl in sels:
    ctl_3cns = (rootctrl.replace("_1_","_3_")).replace("_ctl","_ik_cns")
    High_value = mc.getAttr("%s_distanceDimShape.distance"%rootctrl)
    mDivide1 = "%s_1_mDivide"%rootctrl
    pMAverage2 = "%s_2_pMAverage"%rootctrl
    
    mc.disconnectAttr("%s.output3D"%pMAverage2,"%s_3_mDivide.input1"%rootctrl)
    mc.delete(["%s_3_mDivide"%rootctrl,"%s_4_mDivide"%rootctrl,"%s_5_mDivide"%rootctrl,"%s_6_mDivide"%rootctrl])
    
    mDivide3 = mc.createNode("multiplyDivide",n="%s_3_mDivide"%rootctrl)
    mDivide4 = mc.createNode("multiplyDivide",n="%s_4_mDivide"%rootctrl)
    mDivide5 = mc.createNode("multiplyDivide",n="%s_5_mDivide"%rootctrl)
    mDivide6 = mc.createNode("multiplyDivide",n="%s_6_mDivide"%rootctrl)
    
    mc.setAttr("%s.input2"%mDivide6,High_value,High_value,High_value)
    
    mc.connectAttr("%s.scale"%rootctrl,"%s.input1"%mDivide3)
    mc.connectAttr("chief_C0_ctl.scale","%s.input2"%mDivide3)
    mc.connectAttr("%s.output"%mDivide3,"%s.input1"%mDivide4)
    mc.connectAttr("base_C0_ctl.scale","%s.input2"%mDivide4)
    mc.connectAttr("%s.output"%mDivide4,"%s.input1"%mDivide5)
    mc.connectAttr("global_C0_ctl.scale","%s.input2"%mDivide5)
    mc.connectAttr("%s.output"%mDivide5,"%s.input1"%mDivide6)
    mc.connectAttr("%s.output"%mDivide6,"%s.input1"%mDivide1)
    
    mc.connectAttr("%s.output3Dx"%pMAverage2,"%s.scaleX"%ctl_3cns)
    mc.connectAttr("%s.output3Dz"%pMAverage2,"%s.scaleZ"%ctl_3cns)
