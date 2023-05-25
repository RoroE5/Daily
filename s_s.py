import maya.cmds as mc

sels = mc.ls(sl=True) #选择每个音符的主控制器
for rootctrl in sels:
    ctl_2 = rootctrl.replace("_1_","_2_")
    ctl_4 = rootctrl.replace("_1_","_4_")
    ctl_3cns = (rootctrl.replace("_1_","_3_")).replace("_ctl","_ik_cns")
    ctl_3root = (rootctrl.replace("_1_","_3_")).replace("_ctl","_root")
    lct1 = mc.rename(mc.listRelatives(mc.createNode("locator"),ap=1)[0],"%s_lct"%ctl_2)
    lct2 = mc.rename(mc.listRelatives(mc.createNode("locator"),ap=1)[0],"%s_lct"%ctl_4)
    dDim = mc.rename(mc.listRelatives(mc.createNode("distanceDimShape"),ap=1)[0],"%s_distanceDim"%rootctrl)
    mDivide1 = mc.createNode("multiplyDivide",n="%s_1_mDivide"%rootctrl)
    mDivide2 = mc.createNode("multiplyDivide",n="%s_2_mDivide"%rootctrl)
    mDivide3 = mc.createNode("multiplyDivide",n="%s_3_mDivide"%rootctrl)
    mDivide4 = mc.createNode("multiplyDivide",n="%s_4_mDivide"%rootctrl)
    mDivide5 = mc.createNode("multiplyDivide",n="%s_5_mDivide"%rootctrl)
    mDivide6 = mc.createNode("multiplyDivide",n="%s_6_mDivide"%rootctrl)
    pMAverage1 = mc.createNode("plusMinusAverage",n="%s_1_pMAverage"%rootctrl)
    pMAverage2 = mc.createNode("plusMinusAverage",n="%s_2_pMAverage"%rootctrl)
    
    mc.setAttr("%s.v"%lct1,0)
    mc.setAttr("%s.v"%lct2,0)
    mc.parent(lct1,ctl_2)
    mc.setAttr("%s.t"%lct1,0,0,0)
    mc.setAttr("%s.r"%lct1,0,0,0)
    mc.setAttr("%s.s"%lct1,1,1,1)
    mc.parent(lct2,ctl_4)
    mc.setAttr("%s.t"%lct2,0,0,0)
    mc.setAttr("%s.r"%lct2,0,0,0)
    mc.setAttr("%s.s"%lct2,1,1,1)
    
    mc.connectAttr("%sShape.worldPosition[0]"%lct1,"%sShape.startPoint"%dDim)
    mc.connectAttr("%sShape.worldPosition[0]"%lct2,"%sShape.endPoint"%dDim)
    
    mc.addAttr (rootctrl, ln= "Extrusion" , at ="double"  , min=0.1 , max=2 , dv =1 )
    mc.setAttr("%s.Extrusion"%rootctrl,e=1,k= 1)
    mc.addAttr (rootctrl, ln= "Transparency" , at ="double"  , min=0 , max=1 , dv =0 )
    mc.setAttr("%s.Transparency"%rootctrl,e=1,k= 1)
    
    High_value = mc.getAttr("%s.distance"%dDim)
    
    mc.setAttr("%s.scaleX"%ctl_3cns,l=False)
    # mc.setAttr("%s.scaleY"%ctl_3cns,l=False)
    mc.setAttr("%s.scaleZ"%ctl_3cns,l=False)
    mc.setAttr("%s.input1"%mDivide1,High_value,High_value,High_value)
    mc.setAttr("%s.operation"%mDivide2,2)
    mc.setAttr("%s.operation"%pMAverage1,2)
    mc.setAttr("%s.input3D[0]"%pMAverage1,1,1,1)
    
    mc.connectAttr("%s.Extrusion"%rootctrl,"%s.input2.input2X"%mDivide1)
    mc.connectAttr("%s.Extrusion"%rootctrl,"%s.input2.input2Y"%mDivide1)
    mc.connectAttr("%s.Extrusion"%rootctrl,"%s.input2.input2Z"%mDivide1)
    mc.connectAttr("%s.output"%mDivide1,"%s.input1"%mDivide2)
    mc.connectAttr("%s.distance"%dDim,"%s.input2.input2X"%mDivide2)
    mc.connectAttr("%s.distance"%dDim,"%s.input2.input2Y"%mDivide2)
    mc.connectAttr("%s.distance"%dDim,"%s.input2.input2Z"%mDivide2)
    mc.connectAttr("%s.input2"%mDivide1,"%s.input3D[1]"%pMAverage1)
    mc.connectAttr("%s.output"%mDivide2,"%s.input3D[0]"%pMAverage2)
    mc.connectAttr("%s.output3D"%pMAverage1,"%s.input3D[1]"%pMAverage2)
    mc.connectAttr("%s.output3D"%pMAverage2,"%s.input1"%mDivide3)
    mc.connectAttr("%s.s"%rootctrl,"%s.input2"%mDivide3)
    mc.connectAttr("%s.output"%mDivide3,"%s.input1"%mDivide4)
    mc.connectAttr("chief_C0_ctl.s","%s.input2"%mDivide4)
    mc.connectAttr("%s.output"%mDivide4,"%s.input1"%mDivide5)
    mc.connectAttr("base_C0_ctl.s","%s.input2"%mDivide5)
    mc.connectAttr("%s.output"%mDivide5,"%s.input1"%mDivide6)
    mc.connectAttr("global_C0_ctl.s","%s.input2"%mDivide6)
    mc.connectAttr("%s.output.outputX"%mDivide6,"%s.sx"%ctl_3cns)
    mc.connectAttr("%s.output.outputZ"%mDivide6,"%s.sz"%ctl_3cns)
    
    mc.pointConstraint(ctl_2,ctl_4,"%s|%s"%(rootctrl,ctl_3root),mo=1)
    mc.orientConstraint(ctl_2,ctl_4,"%s|%s"%(rootctrl,ctl_3root),mo=1)
    mc.scaleConstraint(ctl_2,ctl_4,"%s|%s"%(rootctrl,ctl_3root),mo=1)
