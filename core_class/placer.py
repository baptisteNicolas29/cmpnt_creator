from maya import cmds
from PySide2 import QtCore, QtWidgets, QtGui

class Placer:

    def __init__(self, placers, shape_typ= None):

        self.placers= placers
        self.placers_shape= shape_typ

    def create_placer(self, placer_name):

        cmds.createNode('transform', n= placer_name, ss= 1) if not cmds.objExists(placer_name) else placer_name

        if isinstance(shape_typ, str):

            cmds.createNode(self.placers_shape, n= placer_name+ 'Shape', p=placer_name, ss= 1)

        else:
            cmds.setAttr(placer_name+ '.displayHandle', 1)
