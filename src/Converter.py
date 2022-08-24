from math import floor
from .AnimSKB import AnimSKB
from .AnimSKBHeader import AnimSKBHeader
from .AnimSKBKey import AnimSKBKey
from mathutils import Vector, Quaternion, Matrix
import bpy
import json


class Converter:
    def __init__(self):
        pass

    def loadAnimSKB(self, animation_name: str, skb: AnimSKB, armature, reverse_bone_order: bool) -> None:

        # Reset pose
        for pb in armature.pose.bones:
            pb.matrix_basis = Matrix.Identity(4)

        # Create new animation (action)
        armature.animation_data_create()
        armature.animation_data.action = bpy.data.actions.new(
            name=animation_name)

        for frame_id in range(len(skb.offsets)):
            bone_ids = range(len(skb.offsets[frame_id]))
            if (reverse_bone_order):
                bone_ids = reversed(bone_ids)
            for bone_id in bone_ids:
                if len(armature.pose.bones) <= bone_id:
                    break
                skbKey_id = skb.offsets[frame_id][bone_id]
                skbKey = skb.keys[skbKey_id]
                bone = armature.pose.bones[bone_id]
                parentBone = bone.parent
                bone.rotation_quaternion = skbKey.quat
                bone.keyframe_insert(
                    data_path='rotation_quaternion', frame=frame_id)
                if parentBone != None:
                    pt = bone.parent.matrix.translation
                    bone.matrix.translation = pt + \
                        Vector(skbKey.tran)
                else:
                    bone.matrix.translation = Vector(skbKey.tran)
                bone.keyframe_insert(data_path='location', frame=frame_id)
