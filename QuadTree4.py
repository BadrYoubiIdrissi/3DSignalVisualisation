# -*- coding: utf-8 -*-

import numpy as np 
import vtk   as vtk 

#     class that defines a tree structure based on quad

class tree_amr:
    def __init__(self, point_0, point_1, point_2, point_3, point_4, point_5, point_6, point_7, depth, depth_max,
                 dico):

        #     creation of a branch or a leaf 

        #   Be carefull this a recursive function 

        #    inputs:
        #        point_0 : point 0 of the quad  
        #        point_1 : point 1 of the quad   
        #        point_2 : point 2 of the quad   
        #        point_3 : point 3 of the quad  
        #        depth   : depth of the local branch or leaf in the tree 
        #        depth_max : maximum depth allowed in this tree 
        #        dico : it is a dictionnary that includes at least :
        #        dico['eval_function'] : a function used to compute the
        #                                physical value value on a point
        #            inputs :
        #                point : the point of the quad
        #                dico  : the dictionnary that includes all what you need
        #            outputs :
        #                this function returns the physical value estimated at
        #                this point
        #        dico['refine_or_not'] : a function used to decide if the leaf
        #                                should be transformed in a branch
        #            inputs :
        #                value_0 : physical value at point_0 of the quad
        #                value_1 : physical value at point_1 of the quad
        #                value_2 : physical value at point_2 of the quad
        #                value_3 : physical value at point_3 of the quad
        #                dico  : the dictionnary that includes all what you need
        #            outputs :
        #                this function returns True or False 
        #        dico['level_min'] : you must refine at least up to this depth 

        #    quad point order : 

        #                     3-------2                      3---7---2
        #                     |       |                      |   |   |
        #  for a leaf       : |       |  for a branch     :  8---4---6
        #                     |       |                      |   |   |
        #                     0-------1                      0---5---1

        #     first we suppose that when we create it, it is a leaf 
        self.branch = False

        #    store the information locally in the memory for the leaf 
        self.point_0 = point_0
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.point_4 = point_4
        self.point_5 = point_5
        self.point_6 = point_6
        self.point_7 = point_7
        self.depth_max = depth_max
        self.depth = depth
        self.dico = dico
        
        r0 = self.dico['eval_function'](self.point_0,self.dico)
        r1 = self.dico['eval_function'](self.point_1,self.dico)
        r2 = self.dico['eval_function'](self.point_2,self.dico)
        r3 = self.dico['eval_function'](self.point_3,self.dico)
        r4 = self.dico['eval_function'](self.point_4,self.dico)
        r5 = self.dico['eval_function'](self.point_5,self.dico)
        r6 = self.dico['eval_function'](self.point_6,self.dico)
        r7 = self.dico['eval_function'](self.point_7,self.dico)
        
        self.val0 = r0
        self.val1 = r1
        self.val2 = r2
        self.val3 = r3
        self.val4 = r4
        self.val5 = r5
        self.val6 = r6
        self.val7 = r7
        
        if (depth < depth_max):

            #   if the depth of the leaf is lower that the maximum depth 
            #   then we check if we need to transform the leaf into a branch
            #   We must transform the leaf into a branch 
            
            if self.dico['refine_or_not'](r0,r1,r2,r3,r4,r5,r6,7, dico) or depth <= self.dico['level_min']:
                
                self.branch = True
                
                point_4 = (point_0+point_2) / 2
                point_5 = (point_0+point_1) / 2
                point_6 = (point_1+point_2) / 2
                point_7 = (point_2+point_3) / 2
                point_8 = (point_0+point_3) / 2
                
                self.child_up_left = tree_amr(point_8, point_4, point_7, point_3, depth+1, depth_max, dico)
                self.child_up_right = tree_amr(point_4, point_6, point_2, point_7, depth+1, depth_max, dico)
                self.child_down_left = tree_amr(point_0, point_5, point_4, point_8, depth+1, depth_max, dico)
                self.child_down_right = tree_amr(point_5, point_1, point_6, point_4, depth+1, depth_max, dico)
                
    def Create_Mesh_And_Connectivity_List(self, List_Of_Point, Connectivity):
        
        if not self.branch:
            
            List_Of_Point.append(self.point_0)
            List_Of_Point.append(self.point_1)
            List_Of_Point.append(self.point_2)
            List_Of_Point.append(self.point_3)
            n = len(List_Of_Point) - 1
            Connectivity.append(["2D", n-3, n-2, n-1, n])
            
        else:
            self.child_up_left.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)
            self.child_up_right.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)
            self.child_down_left.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)
            self.child_down_right.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)
    
            

    def Get_values(self, List_Of_Values):
        if not self.branch:
            List_Of_Values.append(self.val0)
            List_Of_Values.append(self.val1)
            List_Of_Values.append(self.val2)
            List_Of_Values.append(self.val3)
        
        else:
            
            self.child_up_left.Get_values(List_Of_Values)
            self.child_up_right.Get_values(List_Of_Values)
            self.child_down_left.Get_values(List_Of_Values)
            self.child_down_right.Get_values(List_Of_Values)
            



################################################################################
#
#    part of the module dedicated to check the routines
#
################################################################################

def compute_value(p, dico):
    # scalar function (euclidian distance)
    # It's an example to determine some isolines
    center = dico['center']
    return np.sqrt((p[0] - center[0])**2 + (p[1] - center[1])**2 + (p[2] - center[2])**2)

def test_function(r0, r1, r2, r3, dico):
    # function to choose if the mesh needs to be refined
    # dico['refine_or_not'] : a function used to decide if the leaf should be
    #                         transformed in a branch
    #     inputs :
    #         value_0 : physical value at point_0 of the quad
    #         value_1 : physical value at point_1 of the quad
    #         value_2 : physical value at point_2 of the quad
    #         value_3 : physical value at point_3 of the quad
    #         dico    : the dictionnary that includes all what you need
    #     outputs :
    #         this function returns True or False 
    r_target = dico['r_target']

    if ((r0 <  r_target) | (r1 <  r_target) | (r2 <  r_target) | (r3 <  r_target)) \
     & ((r0 >= r_target) | (r1 >= r_target) | (r2 >= r_target) | (r3 >= r_target)):    
        return True 
    else: 
        return False


def test():
    point_1 = np.asarray([0.0, 0.0, 0.0])
    point_2 = np.asarray([1.0, 0.0, 0.0])
    point_3 = np.asarray([1.0, 1.0, 0.0])
    point_4 = np.asarray([0.0, 1.0, 0.0])
    depth_max = 10
    depth = 0 

    dico = {}  # this dictionnary is used to send any structure to the quad_tree
    dico['eval_function'] = compute_value
    dico['refine_or_not'] = test_function
    dico['center']        = [0.0 , 0.0, 0.0]
    dico['r_target']      = 0.3
    dico['level_min']     = 1

    my_tree = tree_amr(point_1, point_2, point_3, point_4, depth, depth_max,
                       dico)

    List_Of_Point = []
    Connectivity = []
    List_Of_vals = []
    my_tree.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)

    MyVtkFile = vtk.FileVTK('tree_amr_case_3',
                            'quadtree refined using the target function')
    MyVtkFile.SavePoints(List_Of_Point)
    MyVtkFile.SaveConnectivity(Connectivity)
    
    my_tree.Get_values(List_Of_vals)
    
    MyVtkFile.CreatePointScalarSection(List_Of_Point)
    MyVtkFile.SavePointScalar("distance", List_Of_vals)
    
    MyVtkFile.close()

if __name__ == "__main__":
    test()
