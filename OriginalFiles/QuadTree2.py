# -*- coding: utf-8 -*-

import numpy as np 
import vtk   as vtk 

#     class that defines a tree structure based on quad

class tree_amr:
    def __init__(self, point_0, point_1, point_2, point_3, depth, depth_max):

        #     creation of a branch or a leaf 

        #   Be carefull this a recursive function 

        #    inputs:
        #        point_0 : point 0 of the quad  
        #        point_1 : point 1 of the quad   
        #        point_2 : point 2 of the quad   
        #        point_3 : point 3 of the quad  
        #        depth   : depth of the local branch or leaf in the tree 
        #        depth_max : maximum depth allowed in this tree 
        #        eval_function : function to evaluate if we have to transform
        #                        a leaf into branch

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
        
        if (depth < depth_max):

            #    if the depth of the leaf is lower that the maximum depth then
            #    we check if we need to transform the leaf into a branch
            #    We must transform the leaf into a branch 

            #    creation points 4 to 8 that are used to create the new leaves 

            #    creation of the new leaves, this is the recursive part  
            
            print ('tree_amr.init has already been coded')

    def Create_Mesh_And_Connectivity_List(self, List_Of_Point, Connectivity):

        #      inputs :
        #        ListOfPoint : list that already includes points provided by
        #                      another routine
        #        Connectivity : connectivity list that already includes
        #                       information provided by other routines

        #    outputs :
        #        ListOfPoint : you must add to this list the points related
        #                      to this leaf
        #        Connectivity : you must add to this list the connectivity that
        #                       describe your quad

        print ('tree_amr.Create_Mesh_And_Connectivity_List to be coded')

################################################################################
#
#    part of the module dedicated to check the routines
#
################################################################################

def test():
    point_1 = np.asarray([0.0, 0.0, 0.0])
    point_2 = np.asarray([1.0, 0.0, 0.0])
    point_3 = np.asarray([1.0, 1.0, 0.0])
    point_4 = np.asarray([0.0, 1.0, 0.0])
    depth_max = 0
    depth = 0 

    my_tree = tree_amr(point_1, point_2, point_3, point_4, depth, depth_max)
    
    List_Of_Point = []
    Connectivity = []
    my_tree.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)

    MyVtkFile = vtk.FileVTK('tree_amr_case_2',
                            'first time I can see my quadtree')
    MyVtkFile.SavePoints(List_Of_Point)
    MyVtkFile.SaveConnectivity(Connectivity)
    MyVtkFile.close()

if __name__ == "__main__":
    test()
