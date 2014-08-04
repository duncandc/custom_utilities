# Duncan Campbell
# Written: July 23, 2013
# Yale University
# Determine if a point is inside a given polygon or not. A polygon is a list of
# (x,y) pairs. This function returns True or False. This is an implementation
# of the ray casting method.

def main():
    '''
    example showing the use of inside()
    define a square polygon and test points
    plot the test points a color by inside/outside determination
    '''
    import matplotlib.pyplot as plt
    import numpy as np
    
    #define polygon, e.g. a square centered on the origin
    square = [(-1,-1),(-1,1),(1,1),(1,-1),(-1,-1)]
    
    #create some points to test
    x = (np.random.random_sample(100)-0.5)*4.0
    y = (np.random.random_sample(100)-0.5)*4.0
    #format as a list of tuples
    p = zip(x,y)
    
    result = inside(x,y,square)
    
    #unzip polygone to make it easy to plot
    x,y = zip(*square)
    
    #define color of points: inside==blue, outside==red
    color=['red','blue']
    
    #plot polygon and points
    plt.plot(x,y,color='orange')
    for i in range(0,len(p)):
        plt.plot(p[i][0],p[i][1],'o', color=color[result[i]])
    plt.xlim([-2,2])
    plt.ylim([-2,2])
    plt.show()


#this works for individual points.  replaced with a vectorized version.
#def inside(x,y,poly):
#    '''
#    determines if a point is inside a polygon
#    
#    parameters
#    x: x-coordinate of test point
#    y: y-corrdinate of test point
#    poly: a list of (x,y) pairs defining the vertices of the polygon
#    
#    returns
#    True if inside the polygon
#    False if outside the polygon
#    '''
#    
#    n = len(poly)
#    inside = False
#    
#    p1x,p1y = poly[0]
#    for i in range(n+1):
#        p2x,p2y = poly[i % n]
#        if y > min(p1y, p2y):
#            if y <= max(p1y, p2y):
#                if x <= max(p1x, p2x):
#                    if p1y != p2y:
#                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
#                    if p1x == p2x or x <= xints:
#                        inside = not inside
#        p1x,p1y = p2x,p2y
#
#    return inside



def inside(x,y,poly):
    '''
    determines if a point is inside a polygon
    
    parameters
    x: vector of x-coordinates of points to test
    y: vector of y-coordinates of points to test
    poly: a vector of (x,y) pairs defining the vertices of the polygon
    
    returns
    True if inside the polygon
    False if outside the polygon
    '''

    import numpy as np

    x = np.array(x, copy=True)
    y = np.array(y, copy=True)
    poly = np.array(poly, copy=True)

    n = len(poly)
    inside = np.array([False]*len(x))

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        cond1 = (y > min(p1y, p2y))
        cond2 = (y <= max(p1y, p2y))
        cond3 = (x <= max(p1x, p2x))
        cond = np.array(cond1 & cond2 & cond3)
        if p1y != p2y:
            xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
        if p1x == p2x:
            inside[cond] = np.logical_not(inside[cond])
        else:
            cond = cond & (x <= xints)
            inside[cond] = np.logical_not(inside[cond])
        p1x,p1y = p2x,p2y

    return inside

if __name__ == '__main__':
    main()