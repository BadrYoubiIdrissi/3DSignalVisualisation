# -*- coding: utf-8 -*-

import numpy as np

import tri as t
import vtk as vtk

class tetra: 
    """
    A tetrahedron is defined by four points and a four triangles
    the normal of each triangle face should point out of the tetrahedron

    Attributes
    ----------
    
    points : nested list of the 4 tetrahedron vertices 
            (cartesian coordinates)
    
    faces : nested list of the 4 faces
    """

    def __init__(self, point1, point2, point3, point4):
        """
        Create a tetrahedron by storing his 4 vertices and his 4 faces
        
        Inputs
        ------
        
        point1, point2, point3, point4 : the 4 tetrahedron vertices
        """
        
        self.points = []
        self.faces = []

        print ('tetra.init to be coded')

    def Create_Mesh_And_Connectivity_List(self, List_Of_Point, Connectivity):
        """
        Inputs
        ------
        List_Of_Point : list that already includes points provided by another 
                        routine
        Connectivity  : connectivity list that already includes information 
                        provided by other routines

        Outputs
        -------
        List_Of_Point : you must add to this list the points related to this 
                        tetra
        Connectivity : you must add to this list the connectivity that describe
                       your tetra
        """

        print ('tetra.Create_Mesh_And_Connectivity_List to be coded')

    def Create_Mesh_And_Connectivity_List_From_Tri(self, 
                                                   List_Of_Point, 
                                                   Connectivity):
        """
        Inputs
        ------
        List_Of_Point : list that already includes points provided by another
                        routine
        Connectivity  : connectivity list that already includes information 
                        provided by other routines

        Outputs
        -------
        List_Of_Point : you must add to this list the points related to each
                        tri of this tetra
        Connectivity  : you must add to this list the connectivity that 
                        describes each tri of this tetra 
        """
        
        print ('tetra.Create_Mesh_And_Connectivity_List_From_Tri to be coded')

    def distance_to_a_point(self, p):
        """
        Inputs
        ------
        p : it is a point
        
        Outputs
        -------
        [True/False, d_min]
        - True only if one of the face of the tetra is pointing in 
          the direction of point 
        - d_min (if True) minimum distance from the point to the tetra
        """
        outside = False 
        d_min = np.inf        # Numpy Infinity
        
        print ('tetra.distance_to_a_point to be coded ')
        
        return [outside, d_min] 
        

###############################################################################
#
#    Part of the module dedicated to auto-validation 
#
###############################################################################


def test_1(): 

    print ('First test that create two vtk files ')
    print ('   - the first file allows to plot the Tetra')
    print ('   - the second file allows to plot the Tetra and all the normal')
    print ('   of its tri to check if they a pointing in the right direction')
    point1 = np.asarray([0.0, 0.0, 0.0])
    point2 = np.asarray([1.0, 0.0, 0.0])
    point3 = np.asarray([0.0, 1.0, 0.0])
    point4 = np.asarray([0.0, 0.0, 1.0])
    my_tetra = tetra(point1, point2, point3, point4)

    List_Of_Point = []
    Connectivity = []
    my_tetra.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)
    MyVtkFile = vtk.FileVTK('tetra','tetra')
    MyVtkFile.SavePoints(List_Of_Point)
    MyVtkFile.SaveConnectivity(Connectivity)
    MyVtkFile.close()

    List_Of_Point = []
    Connectivity = []
    my_tetra.Create_Mesh_And_Connectivity_List_From_Tri(List_Of_Point, 
                                                        Connectivity)
    MyVtkFile = vtk.FileVTK('tetra_from_tri',
                            'Tri from a tetra and the normal of each face')
    MyVtkFile.SavePoints(List_Of_Point)
    MyVtkFile.SaveConnectivity(Connectivity)
    MyVtkFile.close()

def test_2():

    print ('Second test used to compute the distance of a point from a tetra')
    point1 = np.asarray([0.0, 0.0, 0.0])
    point2 = np.asarray([1.0, 0.0, 0.0])
    point3 = np.asarray([0.0, 1.0, 0.0])
    point4 = np.asarray([0.0, 0.0, 1.0])
    my_tetra = tetra(point1, point2, point3, point4)

    p = np.asarray([0.01, 0.01, 0.01])
    [test, d_min] = my_tetra.distance_to_a_point(p)

    print ('the point is outside the tetra: '+str(test))
    print ('distance min: '+str(d_min))

if __name__ == "__main__":
    test_1()
    test_2()
