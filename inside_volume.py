#!/usr/bin/env python

#Duncan Campbell
#Yale University
#June 17, 2014
#determine if a set of 3D points is inside/outside a volume

from __future__ import division
import numpy as np
from scipy.spatial import cKDTree
import geometry

def main():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import time
    
    cyl = geometry.cylinder(center=geometry.point3D(45,45,45), radius = 5, length=50, normal=np.array([45.0,45.0,45.0]))
    
    N_points = 10000000
    
    test_points = []
    for i in range(0,N_points):
        test_points.append(geometry.point3D(np.random.random(3)*100.0))
    x = np.array([point.x1 for point in test_points])
    y = np.array([point.x2 for point in test_points])
    z = np.array([point.x3 for point in test_points])
    
    start = time.time()
    inside = inside_volume(cyl,test_points)
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


def inside_volume(shape, points):
    
    points = np.array(points)
    values = np.array([point.values() for point in points])
    KDT = cKDTree(values)
    
    points_to_test = np.array(KDT.query_ball_point(shape.center.values(),shape.circum_r()))
    print points_to_test
    inside = shape.inside(points[points_to_test])
    inside = points_to_test[inside]
    
    return inside


if __name__ == '__main__':
    main()