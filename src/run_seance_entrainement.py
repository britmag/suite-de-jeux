# encoding: utf-8
import numpy as np
from scipy import stats
from random import shuffle
from optparse import OptionParser
from bm_io import read_data_file, send_message, send_sms_message
from bm_prob import initialize_named_choices

def training_times(data_dict, max_time):
    """
    Crée un programme d'entrainement sur la base des éléments choisis 
    et un temps maximum.
    """
    keys = data_dict.keys()
    weights = np.array([data_dict[k][2] for k in keys])
    rv = initialize_named_choices(keys, weights)

    sequence = rv.rvs(size=100)
    

    time_left = max_time

    text =  "\nSéance sur %d minutes : \n" % max_time
    for s in sequence:
        if time_left > 0:
            key = keys[s]
            name = data_dict[key][0]
            dur = min(data_dict[key][1], time_left)
            time = stats.poisson.rvs(dur, size=1)
            time_left = time_left - time
            if time > 0:
                text = text +  "  - %s : %d minutes\n" % (name, time)
        else:
            break

    return text

if __name__ == '__main__':

    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--fich", dest="filename",
                      help="Nom fichier avec options, durees, poids.",
                      action="store", type="string")
    parser.add_option("-t", "--dur", dest="duree",
                      help="Duree (en minutes) de la seance.",
                      action="store", type="int")
    parser.add_option("-e", "--email", dest="e_filename",
                      help="Nom fichier avec infos pour envoi email.",
                      action="store", type="string")
    parser.add_option("-s", "--sms", dest="s_filename",
                      help="Nom fichier avec infos pour envoi SMS.",
                      action="store", type="string")

    (options, args) = parser.parse_args()

    data_dict = read_data_file(options.filename)
    text = training_times(data_dict, options.duree)

    if options.e_filename is not None:
        send_message(options.e_filename, text, "Séance d'entrainement")
    if options.s_filename is not None:
        send_sms_message(options.s_filename, text)
    else:
        print text

