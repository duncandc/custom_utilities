#!/usr/bin/env python

from ..geometry import point3D, face, polygon3D, sphere, point2D, polygon2D, circle
from ..geometry import cylinder
import numpy as np
import math

def test_square():
    v1 = point2D(0,0)
    v2 = point2D(1,0)
    v3 = point2D(1,1)
    v4 = point2D(0,1)
    square = polygon2D([v1,v2,v3,v4])
    assert len(square.vertices) == 4, "number of unique vertices is wrong"
    area = square.area(positive=True)
    assert area == 1.0, "area of 1x1 calculation wrong"
    center = square.center().values()
    assert center == (math.sqrt(1.0)/2.0,math.sqrt(1.0)/2.0), "center wrong"
    r = square.circum_r()
    assert r == math.sqrt(2.0)/2.0, "circumscribed radius incorrect"

def test_cube():
    v1 = point3D(0,0,0)
    v2 = point3D(1,0,0)
    v3 = point3D(0,1,0)
    v4 = point3D(1,1,0)
    v5 = point3D(0,0,1)
    v6 = point3D(1,0,1)
    v7 = point3D(0,1,1)
    v8 = point3D(1,1,1)
    f1 = face([v1,v2,v4,v3]) #bottom
    f2 = face([v5,v6,v8,v7]) #top
    f3 = face([v3,v4,v8,v7]) #back
    f4 = face([v1,v2,v6,v5]) #front
    f5 = face([v1,v3,v7,v5]) #left
    f6 = face([v2,v4,v8,v6]) #right
    cube = polygon3D([f1,f2,f3,f4,f5,f6])
    vol = cube.volume()
    assert vol == 1.0, "volume of 1x1x1 calculation wrong"
    assert len(cube.vertices) == 8, "number of unique vertices is wrong"
    assert len(cube.faces) == 6, "number of unique vertices is wrong"
    
def test_circle():
    center = point2D(0,0)
    radius = 1.0
    s = circle(center,radius)
    assert s.area() == math.pi, "area of r=1 sphere calculation wrong"
    assert s.radius == 1.0, "radius of r=1 circle wrong"
    
def test_sphere():
    center = point3D(0,0,0)
    radius = 1.0
    s = sphere(center,radius)
    assert s.volume() == (4.0/3.0)*math.pi, "volume of r=1 sphere calculation wrong"
    assert s.radius == 1.0, "radius of r=1 sphere wrong"
    
def test_distance2D():
    p1 = point2D(0,0)
    p2 = point2D(0,1)
    dist = p1.distance(p2)
    assert dist==1.0, "distance calc incorrect"
    dist = p1.distance_periodic(p2,1.5)
    assert dist==0.5
    
    
def test_distance3D():
    p1 = point3D(0,0,0)
    p2 = point3D(0,1,0)
    dist = p1.distance(p2)
    assert dist==1.0, "distance calc incorrect"
    dist = p1.distance_periodic(p2,1.5)
    assert dist==0.5
    
def test_face():
    v1 = point3D(0,0,1)
    v2 = point3D(1,0,1)
    v3 = point3D(0,1,1)
    v4 = point3D(1,1,1)
    f = face([v1,v2,v4,v3])
    area = f.area()
    assert area==1.0, "area calculation incorrect for 1X1 square face"
    center = f.center().values()
    assert center == (0.5,0.5,1.0)
    n = f.normal()
    assert np.all(n == np.array([0,0,1])), 'incorrect normal'
    
def test_cylinder():
    cyl = cylinder(center=point3D(0.0,0.0,0.0), radius = 2.0, length=4.0, normal=np.array([0.0,0.0,1.0]))
    assert cyl.volume()==math.pi*2.0**2.0*4.0, "incorrect cylinderical volume calc"
    
    test_point = point3D(0,0,0)
    assert cyl.inside(test_point)==True, "inside calculation incorrect"
    test_point = point3D(10,0,0)
    assert cyl.inside(test_point)==False, "inside calculation incorrect"
    
    
    
    
    