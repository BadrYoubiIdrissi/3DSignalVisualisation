# -*- coding: utf-8 -*-

import numpy as np 

from tetra import tetra
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
        self.file = open(DefenseFile)
        self.number_modules = int(self.getNextValue())
        
        for _ in range(self.number_modules):
            center = self.toVector(self.getNextValue())
            base_length = float(self.getNextValue())
            height = float(self.getNextValue())
            rotation = float(self.getNextValue())
            i_z = np.array([0.0,0.0,1.0])
            
            distanceFromCenter = (np.sqrt(3)/3)*base_length # à expliquer
            point1 = center + self.radialVect(rotation)*distanceFromCenter
            point2 = center + self.radialVect(rotation + 120)*distanceFromCenter
            point3 = center + self.radialVect(rotation + 240)*distanceFromCenter
            point4 = center + height*i_z
            
            self.List_Of_Modules.append(tetra(point1, point2, point3, point4))
            
    def getNextValue(self):
        return self.file.readline().strip().split(" : ")[1]
        
    def toVector(self,string):
        arr = string.split(" ")
        arr = [float(e) for e in arr]
        return np.array(arr)
    
    def radialVect(self,angle_in_degrees):
        i_x = np.array([1.0,0.0,0.0])
        i_y = np.array([0.0,1.0,0.0])
        return np.cos(angle_in_degrees*np.pi/180)*i_x + np.sin(angle_in_degrees*np.pi/180)*i_y

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
        for t in self.List_Of_Modules:
            t.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)

    def Distance_Between_a_Point_and_the_Modules(self, p):

        #    inputs : 
        #         - p it is a point
        #    output : [True/False, d_min]
        #         - False if the point is inside one of the defense module 
        #         - d_min = [] list of minimum distance from the point to the
        #                      each defense module

        outside = True
        d_min = []
        
        for t in self.List_Of_Modules:
            [outsidet, d_mint] = t.distance_to_a_point(p)
            outside = outside and outsidet
            d_min.append(d_mint)
        
        return [outside, np.array(d_min)] 


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
