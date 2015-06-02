import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

__all__=['colorline']

def colorline(x, y, v, ax, cmap='cool', vmin=0.0, vmax=1.0, **kwargs):
    """
    plots a line with the color determined by v and a color table
    
    Parameters
    ----------
    x: array_like
    
    y: array_like
    
    v: float
    
    ax: matplotlib.axes
    
    cmap: string specifying color table
    
    Returns
    -------
    line, matplotlib.lines.Line2D
    """
    cmap = plt.get_cmap(cmap) 
    cNorm  = colors.Normalize(vmin=vmin, vmax=vmax)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cmap)
    
    color = scalarMap.to_rgba(v)

    l, = ax.plot(x,y,c=color)
    
    return l