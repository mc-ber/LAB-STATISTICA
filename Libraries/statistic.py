"""
A module that contains functions for statistical analysis ON ARRAYS
"""
import numpy as np

def median(x):
    """A function that determines the median of an array.

    Args:
        x (numpy.ndarray): the array for which the median is to be calculated

    Returns:
        float: the median of the array
    """
    x_sorted = np.sort(x)
    if len(x_sorted)%2 == 0: 
        # even number of elements - returns the average of the two central elements
        m = (x_sorted[int(len(x_sorted)/2)-1] + x_sorted[int(len(x_sorted)/2)])/2
    else: 
        # odd number of elements - returns the central element
        m = x_sorted[int((len(x_sorted)-1)/2)]
    return m

def percentile75(x):
    """A function that determines the value above which lies the 25% of the values.

    Args:
        x (numpy.ndarray): the array for which the median is to be calculated

    Returns:
        float: the value above which lies the 25% of the values
    """
    x_sorted = np.sort(x)
    idx = int(0.75*len(x))
    pv = x_sorted[idx]
    return pv

def percentile25(x):
    """A function that determines the value above which lies the 25% of the values.

    Args:
        x (numpy.ndarray): the array for which the median is to be calculated

    Returns:
        float: the value above which lies the 25% of the values
    """
    x_sorted = np.sort(x)
    idx = int(0.25*len(x))
    pv = x_sorted[idx]
    return pv

def percentile(x,p):
    """A function that determines the value above which lies the a certain fraction of the values.

    Args:
        x (numpy.ndarray): the array for which the percentile is to be calculated
        p (float): the fraction of the values (should be whithin [0,1])

    Returns:
        float: the value above which lies the fraction `p` of the values
    """
    if not (0 < p and p < 1):
        raise ValueError(f'The percentile value p = {p} is not within the range [0,1]')
    x_sorted = np.sort(x)
    idx = int(p*len(x))
    pv = x_sorted[idx]
    return pv

def mean(x):
    """A function that calculates the mean of an array.

    Args:
        x (numpy.ndarray): the array for which the mean is to be calculated

    Returns:
        float: the mean of the array
    """
    m = np.sum(x)/len(x)
    return m

def variance(x):
    """A function that calculates the variance of an array.

    Args:
        x (numpy.ndarray): the array for which the variance is to be calculated

    Returns:
        float: the variance of the array
    """
    m = mean(x)
    m2= mean(x*x)
    return m2-m*m

def stdev(x,bessel=True):
    """A function that calculates the standard deviation of an array.

    Args:
        x (numpy.ndarray): the array for which the standard deviation is to be calculated
        bessel (bool, optional): applies Bessel's correction. Defaults to True.

    Returns:
        float: the standard deviation of the array
    """
    m = mean(x)
    r = x-m
    s = np.sqrt( np.sum(r*r)/(len(x)-1) ) if bessel else np.sqrt( np.sum(r*r)/len(x) )
    return s

def stdev_mean(x,bessel=True):
    """A function that calculates the standard deviation of the mean of an array.

    Args:
        x (numpy.ndarray): the array for which the standard deviation of the mean is to be calculated
        bessel (bool, optional): applies Bessel's correction. Defaults to True.

    Returns:
        float: the standard deviation of the mean of the array
    """
    s = stdev(x,bessel)
    return s/np.sqrt(len(x))
