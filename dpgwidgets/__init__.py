import sys

sys.path.append("./dpgwrap/")

from dearpygui import dearpygui as dpg

from dpgwrap._item import Item, ContextSupport  # avoids circular imports
from dpgwidgets.constants import Registry as _Registry, Key, Mouse
from dpgwidgets.app import Viewport
from dpgwidgets.theme import Font, Theme
from dpgwrap import (
    containers, 
    drawing, 
    node, 
    plotting, 
    widgets,
)

__all__ = [
    # high-level objects
    "Application",
    "Theme",
    "Font",
    # imports
    "containers",
    "drawing",
    "node",
    "plotting",
    "widgets",
    "themes",
    # dearpygui.dearpygui
    "dpg",
]

UPDATE_ON_IMPORT = False

def update_wrappers():
    import importlib
    import dpgwrap
    from dpgwrap import _generate

    _generate.main()

    importlib.reload(dpgwrap)

    for module in dpgwrap.__all__:
        try:
            importlib.import_module(module, dpgwrap)
        except:
            continue


if UPDATE_ON_IMPORT:
    update_wrappers()


# registries
with dpg.font_registry(id=_Registry.FONT.value, label="AppFontRegistry"):
    pass
with dpg.handler_registry(id=_Registry.APPHANDLER.value, label="AppHandlerRegistry"):
    pass
with dpg.texture_registry(id=_Registry.TEXTURE.value, label="AppTextureRegistry"):
    pass
with dpg.value_registry(id=_Registry.VALUE.value, label="AppValueRegistry"):
    pass
