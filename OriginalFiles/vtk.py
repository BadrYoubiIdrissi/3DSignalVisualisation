# -*- coding: utf-8 -*-

import numpy as np 

class FileVTK:

    def __init__(self, FileName, Comment):
        print ('FileVTK.Init function to be coded')    

    def SavePoints(self, PointList):
        print ('FileVTK.SavePoints function to be coded')

    def SaveConnectivity(self, Connectivity):
        print ('FileVTK.SaveConnectivity function to be coded')

    def CreatePointScalarSection(self,Points):
        print ('FileVTK.CreatePointScalarSection function to be coded')

    def SavePointScalar(self, Label, Values):
        print ('FileVTK.SavePointScalar function to be coded')

    def close(self):
        print ('FileVTK.Close function to be coded')

################################################################################
#
#    Part of the module dedicated to auto-validation 
#
################################################################################

def test():
    MyVtkFile = FileVTK('test_file','first test')

    #     create the mesh point list

    Points =[]
    Points.append([0.0, 0.0, 0.0]) # 0
    Points.append([1.0, 0.0, 0.0]) # 1
    Points.append([1.0, 1.0, 0.0]) # 2
    Points.append([0.0, 1.0, 0.0]) # 3
    Points.append([0.0, 0.0, 1.0]) # 4
    Points.append([1.0, 0.0, 1.0]) # 5
    Points.append([1.0, 1.0, 1.0]) # 6
    Points.append([0.0, 1.0, 1.0]) # 7
    Points.append([2.0, 0.0, 0.0]) # 8
    Points.append([2.0, 1.0, 0.0]) # 9
    Points.append([2.0, 1.0, 1.0]) # 10 

    #          7---------------6---------------10
    #         /               /|               |
    #        /               / |               |
    #       4---------------5  |               |
    #       |               |  |               |
    #       |  3------------|--2---------------9    
    #       | /             | /               /
    #       |/              |/               /
    #       0---------------1---------------8
    
    MyVtkFile.SavePoints(Points)

    #     create the connectivity with:
    Connectivity = []
    Connectivity.append(["3D", 1, 8, 2, 5])             # tetrahedron 
    Connectivity.append(["3D", 0, 1, 2, 3, 4, 5, 6 ,7]) # hexahedron  
    Connectivity.append(["2D", 2, 9, 10, 6])            # quadrilateral
    Connectivity.append(["2D", 8, 9, 2])                # triangle
    Connectivity.append(["2D", 5, 10])                  # line 

    MyVtkFile.SaveConnectivity(Connectivity)

    #     create point scalar section

    MyVtkFile.CreatePointScalarSection(Points)

    #    create the data values: distance to point [0.0, 0.0, 0.0]
    Values = []
    for Point in Points:
        Values.append(np.sqrt(Point[0]**2 + Point[1]**2 + Point[2]**2))
    MyVtkFile.SavePointScalar("distance", Values)

    #    create the data values: distance to point [0.0, 0.0, 0.0] time 3.0
    Values = []
    for Point in Points:
        Values.append(3.0 * np.sqrt(Point[0]**2 + Point[1]**2 + Point[2]**2))
    MyVtkFile.SavePointScalar("distance_*_3", Values)

    MyVtkFile.close()

if __name__ == "__main__":
    test()
