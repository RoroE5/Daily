import maya.cmds as mc

sels = mc.ls(sl=True)

# skinlowmod = "A_low_mod"
# firstJnt = ['A_low_skin_0_jnt', 'A_low_skin_1_jnt', 'A_low_skin_2_jnt', 'A_low_skin_3_jnt']
skinlowmod = "lowmod_skin"
firstJnt = ['leaf_chainSpring_skin_1_jnt', 'leaf_chainSpring_skin_2_jnt', 'leaf_chainSpring_skin_3_jnt']

poly_skinCluster = mc.listConnections("%s.inMesh"%skinlowmod,p=0)[0]
poly_bs = mc.listConnections("%s.input[0].inputGeometry"%poly_skinCluster,p=0)[0]


mc.select(cl=1)
for sel in sels:
    nowjnt = ([sel] + mc.listRelatives(sel,ad=1)[::-1])
    lowmod = "lowmod_%d"%int((sel.split("_")[2]).replace("C",""))
    lowmodskinclst = mc.skinCluster(nowjnt,lowmod,tsb=1,bm=1,nw=1,wd=0,mi=8,dr=4,rui=False)[0]
    
    for nj in nowjnt:
        fj = firstJnt[int(nj.split("_")[-2])]
        mc.matchTransform(fj,nj,pos=1)
    
    mc.setAttr("%s.%s"%(poly_bs,lowmod),1)
    mc.copySkinWeights(ss=poly_skinCluster,ds=lowmodskinclst,noMirror=1,surfaceAssociation="closestPoint",influenceAssociation="oneToOne")
    mc.setAttr("%s.%s"%(poly_bs,lowmod),0)
