import maya.cmds as mc
import pymel.core as pm


sourceSkeleton = "og" # source skeleton root joint
targetSkeleton = "new" # target skeleton root joint


# count the joints in the hierarchies
hierarchy1 = []
hierarchy2 = []


sourceSkeletonList = mc.listRelatives(sourceSkeleton, c=True, ad=True, typ='joint')
targetSkeletonList = mc.listRelatives(targetSkeleton, c=True, ad=True, typ='joint')


for bone in sourceSkeletonList:
    hierarchy1.append(bone)

for bone in targetSkeletonList:
    hierarchy2.append(bone)

jointCount1 = (len(hierarchy1))
jointCount2 = (len(hierarchy2))

if jointCount1 != jointCount2:

    mc.error("Oops  -different number of joints in skeletons!")


res1 = [hierarchy1.index(i) for i in hierarchy2]
print hierarchy1
print hierarchy2
print res1


pm.select(hi=True)
for obj in pm.ls(sl=True, dag=True):
        newName = 'OG_' + obj.nodeName()
        pm.rename(obj, newName)

hierarchy1OG = mc.listRelatives(sourceSkeleton, c=True, ad=True, typ='joint')
print hierarchy1OG
sel = mc.select('new', hi=True)

#----------------------------------------

x = 0
for i in res1:

    curJointTarget = hierarchy2[x]
    curJointSource = hierarchy1OG[i]
    mc.parentConstraint(curJointSource, curJointTarget, mo=False)
    print curJointSource
    x = x + 1

min_time = mc.playbackOptions(q=True, min=True)
max_time = mc.playbackOptions(q=True, max=True)
mc.bakeResults(targetSkeletonList, t=(min_time,max_time))
