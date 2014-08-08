#!/usr/bin/env python

#Duncan Campbell
#Yale University
#June 17, 2014
#determine if a set of 3D points is inside/outside a volume

from __future__ import division, print_function
import numpy as np
from HAS.TPCF.kdtrees.ckdtree import cKDTree
import geometry

def main():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import time
    
    cyl = geometry.cylinder(center=(50,95,50), radius = 3, length=20, normal=np.array([0,1,0]))
    period=np.array([100.0,100.0,100.0])
    N_points = 10000000
    
    cyls = []
    for i in range(0,10):
        cp = np.random.random(3)*100.0
        cyl = geometry.cylinder(center=(cp[0],cp[1],cp[2]), radius = 3, length=20, normal=np.array([0,1,0]))
        cyls.append(cyl)
    
    test_points = np.random.random((N_points,3))*100.0
    
    x = test_points[:,0]
    y = test_points[:,1]
    z = test_points[:,2]
    
    start = time.time()
    tree = cKDTree(test_points)
    print("create kdtree time (s): {0}".format(time.time()-start))
    
    start = time.time()
    inside = inside_volume(cyls,tree, period=period)
    #inside = inside_volume(cyl,test_points, period=period)
    print("check points time (s): {0}".format(time.time()-start))
    
    print(inside)
    
    x_inside = x[inside]
    y_inside = y[inside]
    z_inside = z[inside]
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_inside,y_inside,z_inside,'.', color='blue', ms=2)
    ax.plot([cyl.center[0]],[cyl.center[1]],[cyl.center[2]],'x',color='red', ms=10)
    ax.set_xlim([0,100])
    ax.set_ylim([0,100])
    ax.set_zlim([0,100])
    plt.show()
    

def inside_volume(shapes, points, period=None):
    '''
    Check if a list of points is inside a volume.
    parameters
        shape: a geometry.py shape object
        points: a list of points or a ckdtree object
        period: length k array defining axis aligned PBCs. If set to none, PBCs = infinity.
    returns
        True or False if point is inside the volume defined by the shape.
    '''
    
    if type(points) is not cKDTree:
        points = np.array(points)
        KDT = cKDTree(points)
    else:
        KDT=points
    
    if type(shapes) is list:
        result=np.empty((0), dtype=np.int)
        for shape in shapes:
            points_to_test = np.array(KDT.query_ball_point(shape.center,shape.circum_r(),period=period))
    
            if type(points) is cKDTree:
                inside = shape.inside(KDT.data[points_to_test], period)
                inside = points_to_test[inside]
            else:
                inside = shape.inside(points[points_to_test], period)
                inside = points_to_test[inside]
            
            result = np.hstack((result,inside))
        print(result)
        return result
    else:
        shape = shapes
        points_to_test = np.array(KDT.query_ball_point(shape.center,shape.circum_r(),period=period))
    
        if type(points) is cKDTree:
            inside = shape.inside(KDT.data[points_to_test], period)
            inside = points_to_test[inside]
        else:
            inside = shape.inside(points[points_to_test], period)
            inside = points_to_test[inside]
    
        return inside


if __name__ == '__main__':
    main()