from mesh import mesh
from QuadTree3 import tree_amr
from vtk import FileVTK
import numpy as np

isoligne = [1,1.2,1.5]

def signal(p, dico):
    outside, d_min = dico['defZone'].Distance_Between_a_Point_and_the_Modules(p)
    if outside:
        return sum(1/d_min)
    else:
        return 2*max(isoligne)
    
def test_function(r0, r1, r2, r3, dico):
    cond = False
    for iso in dico['r_target']:
        cond = cond or ((r0 <  iso) | (r1 <  iso) | (r2 <  iso) | (r3 <  iso)) \
                        & ((r0 >= iso) | (r1 >= iso) | (r2 >= iso) | (r3 >= iso))
    return cond


defense_zone = mesh("defense_zone.txt")

meshSize = 20.0
meshHeight = 0.01
point1 = np.array([-meshSize, -meshSize, meshHeight])
point2 = np.array([meshSize, -meshSize, meshHeight])
point3 = np.array([meshSize, meshSize, meshHeight])
point4 = np.array([-meshSize, meshSize, meshHeight])

depth_max = 15
depth = 0 

dico = {}  # this dictionnary is used to send any structure to the quad_tree
dico['eval_function'] = signal
dico['refine_or_not'] = test_function
dico['center']        = [0.0 , 0.0, 0.0]
dico['defZone'] = defense_zone
dico['r_target']      = isoligne
dico['level_min']     = 3

my_tree = tree_amr(point1, point2, point3, point4, depth, depth_max,
                   dico)

List_Of_Point = []
Connectivity = []
List_Of_vals = []

defense_zone.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)
List_Of_vals.extend([0]*defense_zone.number_modules*4)

my_tree.Create_Mesh_And_Connectivity_List(List_Of_Point, Connectivity)
my_tree.Get_values(List_Of_vals)

MyVtkFile = FileVTK('Final','Final iso_lines')
MyVtkFile.SavePoints(List_Of_Point)
MyVtkFile.SaveConnectivity(Connectivity)
MyVtkFile.CreatePointScalarSection(List_Of_Point)
MyVtkFile.SavePointScalar("Signal", List_Of_vals)
MyVtkFile.close()


