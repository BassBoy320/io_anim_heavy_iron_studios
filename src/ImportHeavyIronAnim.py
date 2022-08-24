import os
from .Reader import Reader
from .Converter import Converter
from bpy_extras.io_utils import ImportHelper
import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty, CollectionProperty
from bpy.types import Operator, OperatorFileListElement, Armature


def start_import(directory, files, setting_reverse, context):
    for f in files:
        path = directory + f.name
        skb = Reader(path).read()
        active_obj = context.selected_objects[0]
        Converter().loadAnimSKB(f.name, skb, active_obj, setting_reverse)

    return {'FINISHED'}


class ImportHeavyIronAnim(Operator, ImportHelper):
    """Import ANIM Files that were used by Heavy Iron Studios and the Renderware Engine"""
    bl_idname = "import_anim.heavyiron"
    bl_label = "Import Animation(s)"

    filename_ext = ".anm"

    filter_glob: StringProperty(
        default="*.anm",
        options={'HIDDEN'},
        maxlen=255,
    )

    setting_reverse: BoolProperty(
        name="Reverse Bone Order",
        description="",
        default=False,
    )

    files: CollectionProperty(
        type=bpy.types.OperatorFileListElement, options={'HIDDEN'})

    directory: StringProperty(maxlen=1024, default="",
                              subtype='FILE_PATH', options={'HIDDEN'})

    def execute(self, context):
        self.report({'INFO'}, "Started importing...")
        return start_import(self.directory, self.files, self.setting_reverse, context)
