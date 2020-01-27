from maya import cmds
import maya.OpenMaya as om


class Creator:

    """
        name: Creator
        arg: placers | string:list | is the placers list
        arg: jnts_name | string:list | is the controlers list
        desc:
    """

    def __init__(self, placers, jnts_name):

        self.placers= placers
        self.jnt_list= jnts_name

        self.placers_vector= self.set_placers_vector()

    def set_placers_vector(self):

        """
            name: placer_vector
            desc: build vectors of placers
        """
        placers_vector= []

        for node in self.placers:

            placers_vector+= [cmds.xform(node, q= 1, ws= 1, t= 1)]

        return placers_vector

    def align_translate(self, placer_idx):

        """
        name: align_translate
        arg: placer_idx | int | placer index to create alignement
        desc: align translate between placer and bone
        """
        cmds.xform(self.jnt_list[placer_idx], ws= 1, t= (self.placers_vector[placer_idx][0], self.placers_vector[placer_idx][1], self.placers_vector[placer_idx][2]))

    def align_foward_up_rotate(self, placer_idx, up_vec):

        """
            name: align_foward_up_rotate
            arg: placer_idx | int | is the index of the
            arg: up_vec | float:array | is the up vector
            desc:
        """
        x_vec= om.MVector(self.placers_vector[placer_idx+ 1][0]- self.placers_vector[placer_idx][0], self.placers_vector[placer_idx+ 1][1]- self.placers_vector[placer_idx][1], self.placers_vector[placer_idx+ 1][2]- self.placers_vector[placer_idx][2])
        up_vec= om.MVector(up_vec[0], up_vec[1], up_vec[2])
        z_vec= x_vec^ up_vec
        y_vec= z_vec^ x_vec

        x_vec.normalize()
        y_vec.normalize()
        z_vec.normalize()

        vpos= self.placers_vector[placer_idx]

        final_matrix = (x_vec.x, x_vec.y, x_vec.z, 0, y_vec.x, y_vec.y, y_vec.z, 0, z_vec.x, z_vec.y, z_vec.z, 0, vpos[0], vpos[1], vpos[2], 1)
        cmds.xform(self.jnt_list[placer_idx], m= final_matrix, ws= 1)

    def get_normal_plan_vector(self, base_vec, middle_vec, front_vec):

        """
            name: get_normal_plan_vec
            arg: base_vec | float:array | base vector
            arg: middle_vec | float:array | middle vector
            arg: front_vec | float:array | front vector
            return: float:array | normal vector of the plan
            desc:
        """
        baseMiddle_vec= om.MVector(middle_vec[0]- base_vec[0], middle_vec[1]- base_vec[1], middle_vec[2]- base_vec[2])
        middleFront_vec= om.MVector(front_vec[0]- middle_vec[0], front_vec[1]- middle_vec[1], front_vec[2]- middle_vec[2])

        normal_vector= middleFront_vec^ baseMiddle_vec
        return [normal_vector.x, normal_vector.y, normal_vector.z]

    def get_node_vector(self, placer_idx, axe):

        """
            name: get_node_vector
            arg: node_idx | string | index of placer you need
            arg: axe | string | x, y, z depend of axe you want
        """
        axis= ['x', 'y', 'z']
        matrix= cmds.getAttr(self.placers[placer_idx]+ '.worldMatrix')

        return matrix[axis.index(axe)* 4: axis.index(axe)* 4+ 3]

    def build_joints(self):

        for node in self.jnt_list:

            cmds.createNode('joint', n= node) if not cmds.objExists(node) else None
