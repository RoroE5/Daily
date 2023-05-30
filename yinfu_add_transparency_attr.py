import maya.cmds as mc

mc.addAttr ("nameplate_C0_ctl", ln= "Transparency" , at ="double"  , min=0 , max=1 , dv =0 )
mc.setAttr("nameplate_C0_ctl.Transparency",e=1,k= 1)

sels = mc.ls(sl=True) #选择字幕的材质球
reverseNote = mc.listConnections("%s.transparency"%sels[0],p=0)[0]
jpgNote = mc.listConnections("%s.input"%reverseNote,p=0)[0]
mc.disconnectAttr("%s.output"%reverseNote,"%s.transparency"%sels[0])
mc.disconnectAttr("%s.outColor"%jpgNote,"%s.input"%reverseNote)

pMAverage = mc.createNode("plusMinusAverage",n="nameplate_C0_ctl_jpg_pMAverage")

mc.connectAttr("%s.outAlpha"%jpgNote,"%s.input.inputX"%reverseNote)
mc.connectAttr("%s.outAlpha"%jpgNote,"%s.input.inputY"%reverseNote)
mc.connectAttr("%s.outAlpha"%jpgNote,"%s.input.inputZ"%reverseNote)

mc.connectAttr("%s.output"%reverseNote,"%s.input3D[0]"%pMAverage)
mc.connectAttr("nameplate_C0_ctl.Transparency","%s.input3D[1].input3Dx"%pMAverage)
mc.connectAttr("nameplate_C0_ctl.Transparency","%s.input3D[1].input3Dy"%pMAverage)
mc.connectAttr("nameplate_C0_ctl.Transparency","%s.input3D[1].input3Dz"%pMAverage)
mc.connectAttr("%s.output3D"%pMAverage,"%s.transparency"%sels[0])
