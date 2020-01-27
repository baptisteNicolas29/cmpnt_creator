from maya import cmds
from PySide2 import QtCore, QtWidgets, QtGui


"""
    name: __init__
    arg: placers | string:array | name of the placer you want to create
    arg: shape_typ | string | is the shape of placer you will create
    arg: prefix | string | is the prefix of the placers
    arg: suffix | string | is the suffix of the placers
    desc: initialise the class Placer
"""
class Placer:

    def __init__(self, placers, shape_typ= None, prefix= '', suffix= ''):

        self.placers=[]

        for placer in placers:

            self.placers+= ['{0}_{1}_{2}'.format(prefix, placer, suffix)]

        self.placers_shape= shape_typ
        self.prefix, self.suffix= prefix, suffix

    """
        name: create_placer
        arg: placerName | string | name of the placer you want to create
        desc: create placer with gived shaped
    """
    def create_placer(self, placer_name):

        cmds.createNode('transform', n= placer_name, ss= 1) if not cmds.objExists(placer_name) else placer_name

        if isinstance(self.placers_shape, str):

            cmds.createNode(self.placers_shape, n= placer_name+ 'Shape', p= placer_name, ss= 1)

        else:

            cmds.setAttr(placer_name+ '.displayHandle', 1)

    """
        name: create_placers
        arg: placers | string:array | is a list of placers
        desc: create multiple placers
    """
    def create_placers(self, placers= None):

        if not isinstance(self.placers_shape, list):

            placers= self.placers

        for placer in placers:

            self.create_placer(placer)

if __name__ == "__main__":
    pass
