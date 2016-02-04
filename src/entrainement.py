# encoding: utf-8
import numpy as np
from scipy import stats
from random import shuffle
from bm_io import read_data_file, send_message
from bm_prob import initialize_named_choices

def training_times(data_dict, max_time):
    """
    Crée un programme d'entrainement sur la base des éléments choisis 
    et un temps maximum.
    """
    keys = data_dict.keys()
    weights = np.array([data_dict[k][2] for k in keys])
    rv = initialize_named_choices(keys, weights)

    sequence = rv.rvs(size=10)
    

    time_left = max_time

    text =  "\nEntrainement sur %d minutes : \n" % max_time
    for s in sequence:
        if time_left > 0:
            key = keys[s]
            name = data_dict[key][0]
            dur = min(data_dict[key][1], time_left)
            time = stats.poisson.rvs(dur, size=1)
            time_left = time_left - time
            text = text +  "  - %s : %d minutes\n" % (name, time)
        else:
            break

    return text

if __name__ == '__main__':

    duree = 15
    data_dict = read_data_file('positions_britmag.txt')
    text = training_times(data_dict, duree)

    duree = 30
    data_dict = read_data_file('accessoires_britmag.txt')
    text = text + training_times(data_dict, duree)

    duree = 10
    data_dict = read_data_file('plaisirs_britmag.txt')
    text = text + training_times(data_dict, duree)

    send_message('email_entrainement.txt', text, "Séquence d'entrainement")

