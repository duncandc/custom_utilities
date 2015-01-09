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
    
    #define period of box
    period=np.array([100.0,100.0,100.0])
    
    #make some cylinder objects
    cyls = []
    for i in range(0,1000):
        cp = np.random.random(3)*100.0
        cyl = geometry.cylinder(center=(cp[0],cp[1],cp[2]), radius = 1, length=2.5, normal=np.array([cp[0],cp[1],cp[2]]))
        cyls.append(cyl)
    
    #make some test points
    N_points = 10000000
    test_points = np.random.random((N_points,3))*100.0
    x = test_points[:,0]
    y = test_points[:,1]
    z = test_points[:,2]
    
    #create kdtree for points
    start = time.time()
    tree = cKDTree(test_points)
    print("create kdtree time (s): {0}".format(time.time()-start))
    
    #check points against cylinder objects
    start = time.time()
    inside_points, inside_shapes = inside_volume(cyls,tree, period=period)
    print("check points time (s): {0}".format(time.time()-start))
    
    x_inside = x[inside_points]
    y_inside = y[inside_points]
    z_inside = z[inside_points]
    
    
    #plot the points which fall within the cylinders
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_inside,y_inside,z_inside,'.', color='blue', ms=2)
    ax.set_xlim([0,100])
    ax.set_ylim([0,100])
    ax.set_zlim([0,100])
    plt.show()
    
    

def inside_volume(shapes, points, period=None):
    '''
    Check if a list of points is inside a volume.
    parameters
        shape: a geometry.py shape object, or list of objects
        points: a list of points or a ckdtree object
        period: length k array defining axis aligned PBCs. If set to none, PBCs = infinity.
    returns
        inside_points: np.array of ints of indices of points which fall within the 
            specified volumes
        inside_shapes: np.array of booleans, True if any points fall within the shape, 
            False otherwise
    '''
    
    if type(points) is not cKDTree:
        points = np.array(points)
        KDT = cKDTree(points)
    else:
        KDT=points
    
    #if shapes is a list of shapes
    if type(shapes) is list:
        inside_points=np.empty((0,), dtype=np.int)
        inside_shapes=np.empty((len(shapes),), dtype=bool)
        for i, shape in enumerate(shapes):
            points_to_test = np.array(KDT.query_ball_point(shape.center,shape.circum_r(),period=period))
    
            if type(points) is cKDTree:
                inside = shape.inside(KDT.data[points_to_test], period)
                inside = points_to_test[inside]
            else:
                inside = shape.inside(points[points_to_test], period)
                inside = points_to_test[inside]
            if len(inside)>0:
                inside_shapes[i]=True
            else: inside_shapes[i]=False
            inside_points = np.hstack((inside_points,inside))
        inside_points = np.unique(inside_points)
        return inside_points, inside_shapes
    else: #if shapes is a single shape object
        shape = shapes
        points_to_test = np.array(KDT.query_ball_point(shape.center,shape.circum_r(),period=period))
    
        if type(points) is cKDTree:
            inside = shape.inside(KDT.data[points_to_test], period)
            inside = points_to_test[inside]
        else:
            inside = shape.inside(points[points_to_test], period)
            inside = points_to_test[inside]
        
        if len(inside)>0: inside_shapes = True
        else:  inside_shapes = False
        inside_points = inside
        return inside_points, inside_shapes


if __name__ == '__main__':
    main()