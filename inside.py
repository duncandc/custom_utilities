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
    
    #run through each point to check inside/outside
    result = np.empty(100, dtype=int)
    for i in range(0,len(p)):
        result[i] = inside(p[i][0],p[i][1],square)
    
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



def inside(x,y,poly):
    '''
    determines if a point is inside a polygon
    
    parameters
    x: x-coordinate of test point
    y: y-corrdinate of test point
    poly: a list of (x,y) pairs defining the vertices of the polygon
    
    returns
    True if inside the polygon
    False if outside the polygon
    '''

    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

if __name__ == '__main__':
    main()