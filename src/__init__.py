import bpy
from .ImportHeavyIronAnim import ImportHeavyIronAnim
# from .ExportHeavyIronAnim import ExportHeavyIronAnim

bl_info = {
    "name": "Heavy Iron Studios Animation Tools",
    "description": "Import and Export Animation Tools for games like BFBB and TSSM.",
    "author": "BassBoy320",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "location": "File > Import/Export",
    "category": "Import-Export",
    "warning": "This is an early preview. Things like Export are still missing."
}


MENU_TEXT = "Heavy Iron Studios Animation (.anm)"


def menu_func_import(self, context):
    self.layout.operator(ImportHeavyIronAnim.bl_idname, text=MENU_TEXT)


# def menu_func_export(self, context):
    # self.layout.operator(ExportHeavyIronAnim.bl_idname, text=MENU_TEXT)


def register():
    # Import
    bpy.utils.register_class(ImportHeavyIronAnim)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    # Export
    # bpy.utils.register_class(ExportHeavyIronAnim)
    # bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    # Import
    bpy.utils.unregister_class(ImportHeavyIronAnim)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    # Export
    # bpy.utils.unregister_class(ExportHeavyIronAnim)
    # bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
