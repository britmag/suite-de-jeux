import numpy as np
from scipy import stats

def normalize_weights(weights):
    norm_weights = weights / np.float(np.sum(weights))
    return norm_weights

def initialize_named_choices(names, weights):
    xk = np.arange(len(names))
    pk = normalize_weights(weights)
    prob_fn = stats.rv_discrete(values = (xk, pk))
    return prob_fn

def sample_named_choice(names, prob_fn):
    ik = prob_fn.rvs(size=1)
    return names[ik]

#def plot_named_choice_prob(names, prob_fn):
#    xk = np.arange(len(names))
#
#    fig, ax = plt.subplots(1,1)
#    ax.plot(xk, prob_fn.pmf(xk), 'ro', ms=12, mec='r')
#    ax.vlines(xk, 0, prob_fn.pmf(xk), colors='r', lw=4)
#    plt.show()

def setup_uniform_weights(names):
    return np.ones(len(names))

def setup_ordered_weights(names):
    w = np.arange(len(names)) + 1
    return w[::-1]
