# -*- coding: utf-8 -*-

import numpy as np 

class FileVTK:

    def __init__(self, FileName, Comment):
        self.FileName = FileName+".vtk"
        self.file = open(self.FileName, "w")
        self.writel("# vtk DataFile Version 3.1")
        self.writel(Comment)
        self.writel("ASCII")
        print("File: " + self.FileName + " Opened and initiated")

    def SavePoints(self, PointList):
        self.points=PointList
        self.writel("DATASET UNSTRUCTURED_GRID")
        self.writel("POINTS " + str(len(self.points)) + " FLOAT")
        for point in self.points:
            self.writel("  "+str(point[0])+" "+str(point[1])+" "+str(point[2]))
        print("Points saved in "+self.FileName)
        
    def SaveConnectivity(self, Connectivity):
        size = 0
        for c in Connectivity:
            size += len(c)
        self.writel("CELLS "+str(len(Connectivity))+" "+str(size))
        for c in Connectivity:
            self.file.write("  ")
            for i in range(len(c)):
                if i == 0:
                    self.file.write(str(len(c)-1))
                    self.file.write(" ")
                else:
                    self.file.write(str(c[i]))
                    self.file.write(" ")
            self.file.write("\n")
        self.writel("CELL_TYPES "+str(len(Connectivity)))
        for c in Connectivity:
            n = len(c)-1
            if c[0] == "2D":
                if n == 3:
                    celltype = 5
                if n == 4:
                    celltype = 9
                if n == 2:
                    celltype = 3
            else:
                if n == 4:
                    celltype = 10
                if n == 8:
                    celltype = 12
            self.writel("  "+str(celltype))
        print("Connectivity saved")
        
    def CreatePointScalarSection(self,Points):
        self.writel("POINT_DATA "+str(len(Points)))
        
    def SavePointScalar(self, Label, Values):
        self.writel("SCALARS "+Label+" float")
        self.writel("LOOKUP_TABLE default")
        for v in Values:
            self.writel("  "+str(v))
    
    def SaveNormals(self, Normals):
        self.writel("NORMALS cell_normals float")
        for n in Normals:
            self.writel("  {} {} {}".format(n[0],n[1],n[2]))
            
    def writel(self, line):
        self.file.write(line+"\n")
    
    def close(self):
        self.file.close()
        print("File Closed")

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

    print(MyVtkFile.file == open("exemple_cas1.vtk"))
    
    MyVtkFile.close()
    

if __name__ == "__main__":
    test()
