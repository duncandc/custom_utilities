import math
import numpy as np


class point2D(object):
    def __init__(self, x=0.0, y=0.0):
        self.x1 = x
        self.x2 = y

    def distance(self,point2D):
        return math.sqrt((self.x1-point2D.x1)**2.0+(self.x2-point2D.x2)**2.0)
        
    def values(self):
        return self.x1, self.x2


class point3D(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x1 = x
        self.x2 = y
        self.x3 = z
        
    def distance(self,point3D):
        return math.sqrt((self.x1-point3D.x1)**2.0+(self.x2-point3D.x2)**2.0\
        +(self.x3-point3D.x3)**2.0)
        
    def values(self):
        return self.x1, self.x2, self.x3


class polygon2D(object):
    def __init__(self,v=[]):
        self.vertices = v # list of point objects
    
    def area(self,positive=False):
        A = 0.0
        for i in range(0,len(self.vertices)-1):
            A += 0.5*(self.vertices[i].x1*self.vertices[i+1].x2\
                 -self.vertices[i+1].x1*self.vertices[i].x2)
        if positive==True: return math.fabs(A)
        else: return A
        
    def center(self):
        Cx = 0.0
        Cy = 0.0
        A = self.area()
        print A
        for i in range(0,len(self.vertices)-1):
            Cx += 1.0/(6.0*A)*(self.vertices[i].x1+self.vertices[i+1].x1)\
                 *(self.vertices[i].x1*self.vertices[i+1].x2\
                 -self.vertices[i+1].x1*self.vertices[i].x2)
            Cy += 1.0/(6.0*A)*(self.vertices[i].x2+self.vertices[i+1].x2)\
                 *(self.vertices[i].x1*self.vertices[i+1].x2\
                 -self.vertices[i+1].x1*self.vertices[i].x2)
        return point2D(Cx,Cy)
        
    def circum_r(self):
        d = 0.0
        for i in range(0,len(self.vertices)):
            print self.center().distance(self.vertices[i])
            print max(d,self.center().distance(self.vertices[i]))
            d = max(d,self.center().distance(self.vertices[i]))
        return d


class circle(object):
    def __init__(self,center=point2D(0.0,0.0), r=0.0):
        self.center = center
        self.radius = r
    
    def area(self):
        return math.pi*self.radius**2.0
        


class face(object):
    def __init__(self,v=[point3D(0.0,0.0,0.0),point3D(0.0,0.0,0.0),point3D(0.0,0.0,0.0)]):
        self.vertices = v
        #check to see if vertices are co-planer
        if len(self.vertices)<3: 
            raise ValueError('not enough vertices to define face, N must be >=3')
        if len(self.vertices)>3:
            v0 = (self.vertices[0].x1, self.vertices[0].x2, self.vertices[0].x3)
            v1 = (self.vertices[1].x1-v0[0], self.vertices[1].x2-v0[1], self.vertices[1].x3-v0[2])
            v2 = (self.vertices[2].x1-v0[0], self.vertices[2].x2-v0[1], self.vertices[2].x3-v0[2])
            for i in range(3,len(v)):
                v3 = (self.vertices[i].x1-v0[0], self.vertices[i].x2-v0[1], self.vertices[i].x3-v0[2])
                xprd = np.cross(v2,v3)
                vol = np.dot(v1,xprd)
                if vol != 0.0 :raise ValueError('vertices are not co-planer')
    
    def __iter__(self):
        self.start = 0
        self.stop = len(self.vertices)
        return self

    def next(self):
        start = self.start
        if start == self.stop: raise StopIteration
        else:
            self.start += 1
            return self.vertices[start]
            
    def area(self):
        v0 = np.array((self.vertices[0].x1, self.vertices[0].x2, self.vertices[0].x3))
        v1 = np.array((self.vertices[1].x1-v0[0], self.vertices[1].x2-v0[1], self.vertices[1].x3-v0[2]))
        v2 = np.array((self.vertices[2].x1-v0[0], self.vertices[2].x2-v0[1], self.vertices[2].x3-v0[2]))
        v3 = np.cross(v1,v2)
        v4 = np.cross(v3,v1)
        e1 = v1/math.sqrt(v1[0]**2.0+v1[1]**2.0+v1[2]**2.0)
        e2 = v4/math.sqrt(v4[0]**2.0+v4[1]**2.0+v4[2]**2.0)
        x = np.empty(len(self.vertices))
        y = np.empty(len(self.vertices))
        for i, vertex in enumerate(self.vertices):
            x[i] = (vertex.x1-v0[0])*e1[0]+(vertex.x2-v0[1])*e1[1]+(vertex.x3-v0[2])*e1[2]
            y[i] = (vertex.x1-v0[0])*e2[0]+(vertex.x2-v0[1])*e2[1]+(vertex.x3-v0[2])*e2[2]
        A = 0.0
        for i in range(0,len(self.vertices)-1):
            A += 0.5*(x[i]*y[i+1]-x[i+1]*y[i])
        return A
        
    def center(self):
        v0 = np.array((self.vertices[0].x1, self.vertices[0].x2, self.vertices[0].x3))
        v1 = np.array((self.vertices[1].x1-v0[0], self.vertices[1].x2-v0[1], self.vertices[1].x3-v0[2]))
        v2 = np.array((self.vertices[2].x1-v0[0], self.vertices[2].x2-v0[1], self.vertices[2].x3-v0[2]))
        v3 = np.cross(v1,v2)
        v4 = np.cross(v3,v1)
        e1 = v1/math.sqrt(v1[0]**2.0+v1[1]**2.0+v1[2]**2.0)
        e2 = v4/math.sqrt(v4[0]**2.0+v4[1]**2.0+v4[2]**2.0)
        x = np.empty(len(self.vertices))
        y = np.empty(len(self.vertices))
        for i, vertex in enumerate(self.vertices):
            x[i] = (vertex.x1-v0[0])*e1[0]+(vertex.x2-v0[1])*e1[1]+(vertex.x3-v0[2])*e1[2]
            y[i] = (vertex.x1-v0[0])*e2[0]+(vertex.x2-v0[1])*e2[1]+(vertex.x3-v0[2])*e2[2]
        Cx = 0.0
        Cy = 0.0
        A = self.area()
        for i in range(0,len(self.vertices)-1):
            Cx += 1.0/(6.0*A)*(x[i]+x[i+1])*(x[i]*y[i+1]-x[i+1]*y[i])
            Cy += 1.0/(6.0*A)*(y[i]+y[i+1])*(x[i]*y[i+1]-x[i+1]*y[i])
        Cxx = v0[0] + e1[0]*Cx+e2[0]*Cy
        Cyy = v0[1] + e1[1]*Cx+e2[1]*Cy
        Czz = v0[2] + e1[2]*Cx+e2[2]*Cy
        return point3D(Cxx,Cyy,Czz)
        
    def normal(self):
        v0 = self.center().values()
        v1 = (self.vertices[1].x1-v0[0], self.vertices[1].x2-v0[1], self.vertices[1].x3-v0[2])
        v2 = (self.vertices[2].x1-v0[0], self.vertices[2].x2-v0[1], self.vertices[2].x3-v0[2])
        n = np.cross(v1,v2)
        n = n/(math.sqrt(n[0]**2.0+n[1]**2.0+n[2]**2.0))
        return n
        
    


class polygon3D(object):
    def __init__(self,f=[]):
        self.faces = f # list of point objects
        unq_verts = list({vert.values() for sublist in self.faces for vert in sublist})
        self.vertices = [point3D(unq_verts[i][0],unq_verts[i][1],unq_verts[i][2])\
                         for i in range(len(unq_verts))] 
    def volume(self):
        vol = 0.0
        for f in self.faces: # the faces
            n = len(f.vertices)
            v2 = f.vertices[0] # the pivot of the fan
            x2 = v2.x1
            y2 = v2.x2
            z2 = v2.x3
            for i in range(1,n-1): # divide into triangular fan segments
                v0 = f.vertices[i]
                x0 = v0.x1
                y0 = v0.x2
                z0 = v0.x3
                v1 = f.vertices[i+1]
                x1 = v1.x1
                y1 = v1.x2
                z1 = v1.x3
                # Add volume of tetrahedron formed by triangle and origin
                vol += math.fabs(x0 * y1 * z2 + x1 * y2 * z0 \
                                 + x2 * y0 * z1 - x0 * y2 * z1 \
                                 - x1 * y0 * z2 - x2 * y1 * z0)
        return vol/6.0


class sphere(object):
    def __init__(self,center=point3D(0.0,0.0,0.0), r=0.0):
        self.center = center
        self.radius = r
    
    def volume(self):
        return (4.0/3.0)*math.pi*self.radius**3.0
