#!/usr/bin/env python

#Duncan Campbell
#September 2, 2012
#Yale University
#Setup file paths for common systems I work on.

__all__=['get_system','get_base_path','get_data_path','get_output_path','get_plot_path']


def known_systems():
    return ['donuts', 'donut-hole', 'esca', 'rgot', 'omega']


def get_system():
    """
    get the name of the system
    """
    
    import os, sys
    path_to_home = os.getenv("HOME")
    
    host = os.popen('echo $HOSTNAME').read()
    host = host.split('.')[0]
    
    if host in known_systems(): return host
    else:
        host = None
        if os.path.isfile(os.getenv("HOME")+'/.donut-hole'): host = 'donut-hole'
        elif os.path.isfile(os.getenv("HOME")+'/.omega'): host = 'omega'
        else: raise ValueError('unknown system.')
        return host

def get_base_path(node=None):
    """
    get the base path for the system
    """
    
    if node==None: node = get_system()

    if node=='donuts':
        path = '/scratch/dac29/'
    elif node=='donut-hole':
        path = '/Users/duncan/Documents/'
    elif node=='rgot':
        path = '/scratch/dac29/'
    elif node=='esca':
        path = '/scratch/dac29/'
    elif node=='omega':
        path = '/home/fas/padmanabhan/dac29/'
    else:
        return 'error: unknown data directory for this enviorment!'

    return path


def get_data_path(node=None):
    """
    get the base path to data storage for the system
    """
    
    if node==None: node = get_system()

    if node=='donuts':
        path = '/scratch/dac29/data/'
    elif node=='donut-hole':
        path = '/Users/duncan/Documents/projects/data/'
    elif node=='rgot':
        path = '/scratch/dac29/data/'
    elif node=='esca':
        path = '/scratch/dac29/data/'
    elif node=='omega':
        path = '/home/fas/padmanabhan/dac29/scratch/data/'
    else:
        return 'error: unknown data directory for this enviorment!'

    return path

def get_output_path(node=None):
    """
    get the base path to output storage for the system
    """
    
    if node==None: node = get_system()

    if node=='donuts':
        path = '/scratch/dac29/output/'
    elif node=='donut-hole':
        path = '/Users/duncan/Documents/projects/output/'
    elif node=='rgot':
        path = '/scratch/dac29/output/'
    elif node=='esca':
        path = '/scratch/dac29/output/'
    elif node=='omega':
        path = '/home/fas/padmanabhan/dac29/scratch/output/'
    else:
        return 'error: unknown data directory for this enviorment!'

    return path


def get_plot_path(node=None):
    """
    get the base path to plot storage for the system
    """
    
    if node==None: node = get_system()

    if node=='donuts':
        path = '/scratch/dac29/plots/'
    if node=='donut-hole':
        path = '/Users/duncan/Documents/projects/plots/'
    elif node=='rgot':
        path = '/scratch/dac29/plots/'
    elif node=='esca':
        path = '/scratch/dac29/plots/'
    elif node=='omega':
        path = '/home/fas/padmanabhan/dac29/scratch/plots/'
    else:
        return 'error: unknown data directory for this enviorment!'

    return path


