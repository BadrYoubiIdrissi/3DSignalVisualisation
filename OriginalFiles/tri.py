# -*- coding: utf-8 -*-

import numpy as np 
import vtk   as vtk


class tri: 
    
    """
    A triangle is defined by three points and a normal
    
    The normal of the triangle face is defined by 
    N = P1P2 x P1P3 
    
    where x is the cross product and abs(N) = 1

    Attributes
    ----------
    points : nested list of the three triangle vertices 
            (cartesian coordinates)
        
    normal : normal of the triangle (vector components)       
    """

    def __init__(self, point1, point2, point3):

        """
        Create a triangle by computing the normal and by storing the three 
        vertices as attributes
        
        Inputs
        -----
        point1, point2, point3 : the three triangle vertices
                                (cartesian coordinates)
        """     

        print ('tri.init to be coded')

    def Create_Mesh_And_Connectivity_List(self, List_Of_Point, Connectivity):

        """
        The three vertices of the new triangle are stored in List_of_Point and 
        Connectivity
        
        Inputs/Outputs
        --------------
        List_Of_Point : nested list of points of triangles 
                        (cartesian coordinates)
        
        Connectivity  : nested list of connectivity indices over each triangle 
                        vertex (array indices)
        """

        print ('tri.Create_Mesh_And_Connectivity_List to be coded')

    def Create_Tri_and_Normal_Mesh_Connectivity_List(self, List_Of_Point, 
                                                     Connectivity):

        """
        The three vertices of the new triangle and the two points used to
        plot the normal are stored in List_of_Point and Connectivity
        
        Inputs / Outputs
        ----------------

        List_Of_Point : nested list of points of triangles and their normals 
                        (cartesian coordinates)
        
        Connectivity  : nested list of connectivity indices of triangle vertex 
                        and their normals (array indices) 
        """

        print ('tri.Create_Tri_and_Normal_Mesh_Connectivity_List to be coded')

    def distance_to_a_point(self, p):

        """
        Compute the minimum distance from a point to one of the triangle
        vertex.
        
        Input
        -----

        p : point (cartesian coordinates)

        Returns
        -------
        
        distance_to_a_point : list [True/False, d_min]
          - True only if the face is pointing in the direction of point 
          - d_min : minimum distance from the point to the face
        """

        # first we check if the face is pointing toward the point
        
        normal_side = False
        d_min = np.inf                   # Numpy Infinity

        print ('tri.distance_to_a_point to be coded ')

        return [normal_side, d_min]

###############################################################################
#
#    Part of the module dedicated to auto-validation 
#
###############################################################################

def test_1(): 

    print ('\n First test used to plot the tri and its normal \n')
    # When a tri is defined like that, the normal should face toward Z > 0  
    p1 = np.asarray([0.0, 0.0, 0.0])
    p2 = np.asarray([1.0, 0.0, 0.0])
    p3 = np.asarray([0.0, 1.0, 0.0])
    my_tri = tri(p1, p2, p3)

    List_Of_Point = []
    Connectivity = []

    my_tri.Create_Tri_and_Normal_Mesh_Connectivity_List(List_Of_Point, 
                                                        Connectivity)

    MyVtkFile = vtk.FileVTK('tri',
                            'tri with its normal that should face toward Z>0')
    MyVtkFile.SavePoints(List_Of_Point)
    MyVtkFile.SaveConnectivity(Connectivity)
    MyVtkFile.close()

def test_2():
    
    print ('\n Second test used to check the distance' 
           'from a point to the tri ')
    # In this test case you will compute the distance min
    # between a point p and a triangle vertex
    p1 = np.asarray([0.0, 0.0, 0.0])
    p2 = np.asarray([1.0, 0.0, 0.0])
    p3 = np.asarray([0.0, 1.0, 0.0])
    my_tri = tri(p1, p2, p3)

    p = np.asarray([0.0, 0.0, 10.0])
    print ('test of point : '+str(p))
    [test, dist_min] = my_tri.distance_to_a_point(p)
    print ('test     : '+str(test))
    print ('dist_min : '+str(dist_min))
    print ('')

    p = np.asarray([0.0, 0.0, -10.0])
    print ('test of point : '+str(p))
    [test, dist_min] = my_tri.distance_to_a_point(p)
    print ('test     : '+str(test))
    print ('dist_min : '+str(dist_min))
    print ('')

if __name__ == "__main__":
    test_1()
    test_2()

