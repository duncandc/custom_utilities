def spheredist(ra1, dec1, ra2, dec2):
    """
    Returns angular seperation in degrees.  Inputs in degrees.
    """
    from numpy import  degrees, arccos, clip

    x1, y1, z1 = _spherical_to_cartesian(ra1, dec1)
    x2, y2, z2 = _spherical_to_cartesian(ra2, dec2)

    dot = x1*x2+y1*y2+z1*z2
    dot = clip(dot,-1.000000,1.000000)
    da = arccos(dot)
    da = degrees(da)
    
    return da

def _spherical_to_cartesian(ra, dec):
    """
    (Private internal function)
    Inputs in degrees. Outputs x,y,z
    """
    from numpy import radians, sin, cos

    rar = radians(ra)
    decr = radians(dec)

    x = cos(rar) * cos(decr)
    y = sin(rar) * cos(decr)
    z = sin(decr)
 
    return x, y, z
