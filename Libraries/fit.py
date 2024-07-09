from scipy.stats import norm
from scipy.stats import expon


def mod_total (bin_edges, N_signal, mu, sigma, N_background, tau):
    return N_signal * norm.cdf (bin_edges, mu, sigma) + \
            N_background * expon.cdf (bin_edges, 0, tau )
            
            
            
            
def mod_signal_unb (x, mu, sigma) :
    return norm.pdf(x, mu, sigma)
    
    
    
    
def func_approx (x, N_events, mean, sigma, bin_width) :
    return N_events * norm.pdf (x, mean, sigma) * bin_width
