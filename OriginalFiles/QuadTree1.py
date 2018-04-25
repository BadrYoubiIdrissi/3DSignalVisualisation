# -*- coding: utf-8 -*-

import numpy as np 
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

            #   if the depth of the leaf is lower that the maximum depth 
            #   then we check if we need to transform the leaf into a branch
            #   We must transform the leaf into a branch 
            
            print ('depth < depth_max')
                
            #   creation points 4 to 8 that are used to create the new leaves 
            
            #   creation of the new leaves, this is the recursive part
            # self.child_up_left    = 
            # self.child_up_right   = 
            # self.child_down_left  = 
            # self.child_down_right = 
            

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
    depth_max = 3
    depth = 0 

    my_tree = tree_amr(point_1, point_2, point_3, point_4, depth, depth_max)

    print ('Every thing seems OK ')

if __name__ == "__main__":
    test()
