import math


class point2D(object):
    def __init__(self, x=0.0, y=0.0):
        self.x1 = x
        self.x2 = y

    def distance(self,point2D):
        return math.sqrt((self.x1-point2D.x1)**2.0+(self.x2-point2D.x2)**2.0)


class point3D(object):
    def __init__(self):
        self.x1 = 0.0
        self.x2 = 0.0
        self.x3 = 0.0
        
    def distance(self,point3D):
        return math.sqrt((self.x1-point3D.x1)**2.0+(self.x2-point3D.x2)**2.0\
        +(self.x3-point3D.x3)**2.0)


class polygon2D(object):
    def __init__(self,v=[]):
        self.vertices = v # list of point objects
    
    def area(self):
        A = 0.0
        for i in range(0,len(self.vertices)-1):
            A += 0.5*(self.vertices[i].x1*self.vertices[i+1].x2\
                 -self.vertices[i+1].x1*self.vertices[i].x2)
        return A
        
    def center(self):
        Cx = 0.0
        Cy = 0.0
        A = self.area()
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
            d = max(d,self.center().distance(self.vertices[i]))
        return d


class circle(object):
    def __init__(self,center=point2D(0.0,0.0), r=0.0):
        self.center = center
        self.radius = r
    
    def area(self):
        return math.pi*self.radius**2.0
        


class polygon3D(object):
    def __init__(self,f=[]):
        self.faces = f # list of polygon objects
    
    def volume(self):
        A = 0.0
        for i in range(0,len(self.vertices)-1):
            A += 0.5*(self.vertices[i].x1*self.vertices[i+1].x2\
                 -self.vertices[i+1].x1*self.vertices[i].x2)
        return A
        
    def center(self):
        Cx = 0.0
        Cy = 0.0
        Cz = 0.0
        A = self.area()
        for i in range(0,len(self.vertices)-1):
            Cx += 1.0/(6.0*A)*(self.vertices[i].x1+self.vertices[i+1].x1)\
                 *(self.vertices[i].x1*self.vertices[i+1].x2\
                 -self.vertices[i+1].x1*self.vertices[i].x2)
            Cy += 1.0/(6.0*A)*(self.vertices[i].x2+self.vertices[i+1].x2)\
                 *(self.vertices[i].x1*self.vertices[i+1].x2\
                 -self.vertices[i+1].x1*self.vertices[i].x2)
        return point3D(Cx,Cy,Cz)
        
    def circum_r(self):
        d = 0.0
        for i in range(0,len(self.vertices)):
            d = max(d,self.center().distance(self.vertices[i]))
        return d


class sphere(object):
    def __init__(self,center=point3D(0.0,0.0,0.0), r=0.0):
        self.center = center
        self.radius = r
    
    def volume(self):
        return (4.0/3.0)*math.pi*self.radius**3.0
