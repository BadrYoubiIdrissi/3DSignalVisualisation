# -*- coding: utf-8 -*-

import numpy as np 

import tetra as t
import vtk as vtk

class mesh:

    # a mesh contains two lists
    #   - a list of tetra that simulate the defense modules
       
    # attributes of the mesh class
    # self.List_Of_Modules = []

    def __init__ (self, DefenseFile):

        # input : 
        #    - DefenseFile, it is a text file that contains the description of
        #      all defense module
        # output : 
        #    - initialise the attribute self.List_Of_Module 

        self.List_Of_Modules = []
        # Now open DefenseFile, read it and extract information
        print ('To be coded')
        # Then add a tetra to self.List_Of_Modules
        print ('To be coded')
 

    def Create_Mesh_And_Connectivity_List(self, List_Of_Point, Connectivity):

        #     inputs :
        #        - List_Of_Point : list that already includes points provided
        #                          by another routine
        #        - Connectivity : connectivity list that already includes
        #                         information provided by other routines

        #    outputs :
        #        - List_Of_Point : you must add to this list the points
        #                          related to all the tetra of this mesh
        #        - Connectivity : you must add to this list the connectivity
        #                         that describe all the tetra of this mesh
        print ('To be coded')

    def Distance_Between_a_Point_and_the_Modules(self, p):

        #    inputs : 
        #         - p it is a point
        #    output : [True/False, d_min]
        #         - False if the point is inside one of the defense module 
        #         - d_min = [] list of minimum distance from the point to the
        #                      each defense module

        outside = False
        d_min = []
        
        print ('tetra.distance_to_a_point to be coded ')
        
        return [outside, d_min] 

################################################################################
#
#    Part of the module dedicated to auto-validation 
#
################################################################################

def test_1():

    print ('Test 1 used to create the vtk file to plot the defense zone')

    defense_zone = mesh("defense_zone.txt")

    List_Of_Point = []
    Connectivity = []

    defense_zone.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)
    MyVtkFile = vtk.FileVTK('defense_zone','all the tetra in your defense zone')
    MyVtkFile.SavePoints(List_Of_Point)
    MyVtkFile.SaveConnectivity(Connectivity)
    MyVtkFile.close()

def test_2():

    print ('Test 2 return all the distances from the tetras and a point')
    defense_zone = mesh("defense_zone.txt")

    p = np.asarray([0.0, 0.0, 0.0])

    [test, d_min] = defense_zone.Distance_Between_a_Point_and_the_Modules(p)

    print ('the point is outside the defense modules: '+str(test))
    print ('distance min: '+str(d_min))

if __name__ == "__main__":
    test_1()
    test_2()
