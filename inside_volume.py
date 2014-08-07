#!/usr/bin/env python

#Duncan Campbell
#Yale University
#June 17, 2014
#determine if a set of 3D points is inside/outside a volume

from __future__ import division
import numpy as np
#from scipy.spatial import cKDTree
from HAS.TPCF.kdtrees.ckdtree import cKDTree
import geometry

def main():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import time
    
    cyl = geometry.cylinder(center=(98,98,98), radius = 1, length=10, normal=np.array([45.0,45.0,45.0]))
    period=np.array([100.0,100.0,100.0])
    N_points = 10000000
    
    test_points = np.random.random((N_points,3))*100.0
    
    print test_points.shape
    
    x = test_points[:,0]
    y = test_points[:,1]
    z = test_points[:,2]
    
    print x.shape
    
    start = time.time()
    inside = inside_volume(cyl,test_points, period=period)
    print time.time()-start
    
    x_inside = x[inside]
    y_inside = y[inside]
    z_inside = z[inside]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_inside,y_inside,z_inside,'.', color='blue')
    ax.set_xlim([0,100])
    ax.set_ylim([0,100])
    ax.set_zlim([0,100])
    plt.show()


def inside_volume(shape, points, period=None):
    
    points = np.array(points)
    KDT = cKDTree(points)
    
    points_to_test = np.array(KDT.query_ball_point(shape.center,shape.circum_r(),period=period))
    print points_to_test
    inside = shape.inside(points[points_to_test], period)
    inside = points_to_test[inside]
    
    return inside


if __name__ == '__main__':
    main()