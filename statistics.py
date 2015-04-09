import numpy as np

def binned_std(x,bins,bin_key,value_key):

    inds = np.digitize(x[bin_key],bins=bins)
    result = np.empty(len(bins)-1)
    for i in range(0,len(bins)-1):
        in_bin = (inds== i+1)
        result[i] = np.std(x[value_key][in_bin])
        
    return bins, result

def binned_mean(x,bins,bin_key,value_key):

    inds = np.digitize(x[bin_key],bins=bins)
    result = np.empty(len(bins)-1)
    for i in range(0,len(bins)-1):
        in_bin = (inds== i+1)
        result[i] = np.mean(x[value_key][in_bin])
        
    return bins, result