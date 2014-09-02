def get_data_path():

    import platform
    node = platform.node()

    if node=='donuts.astro.yale.edu':
        path = '/scratch/dac29/data/'
    elif node=='login-0-0.local':
        path = '/home/fas/padmanabhan/dac29/scratch/data/'
    elif node=='rgot.astro.yale.edu':
        path = '/scratch/dac29/data/'
    elif node=='esca.astro.yale.edu':
        path = '/scratch/dac29/data/'
    else:
        return 'error: unknown data directory for this enviorment!'

    return path

def get_output_path():

    import platform
    node = platform.node()

    if node=='donuts.astro.yale.edu':
        path = '/scratch/dac29/output/'
    elif node=='login-0-0.local':
        path = '/home/fas/padmanabhan/dac29/scratch/output/'
    elif node=='rgot.astro.yale.edu':
        path = '/scratch/dac29/output/'
    elif node=='esca.astro.yale.edu':
        path = '/scratch/dac29/output/'
    else:
        return 'error: unknown output directory for this enviorment!'

    return path

def get_plot_path():

    import platform
    node = platform.node()

    if node=='donuts.astro.yale.edu':
        path = '/scratch/dac29/plots/'
    elif node=='login-0-0.local':
        path = '/home/fas/padmanabhan/dac29/scratch/output/'
    elif node=='rgot.astro.yale.edu':
        path = '/scratch/dac29/plots/'
    elif node=='esca.astro.yale.edu':
        path = '/scratch/dac29/plots/'
    else:
        return 'error: unknown output directory for this enviorment!'

    return path
