# encoding: utf-8
import numpy as np
from scipy import stats
from random import shuffle
from optparse import OptionParser
from bm_io import read_data_file, send_message, read_sequence_file
from bm_prob import initialize_named_choices

def sequence(step_list):
    """
    Crée un programme d'entrainement sur la base des éléments choisis 
    et un temps maximum.
    """

    text =  "\nDéroulé de votre séance : \n" 

    # go through the steps
    for step in step_list:
        parts = step[0]
        max_time = step[1]
        unite = step[2]
        n_parts = len(parts)
        # go through the parts in the step
        dur_parts = []
        for ipart in xrange(n_parts):
            # read the options
            part = parts[ipart]
            data_dict = read_data_file(part)
            keys = data_dict.keys()
            weights = np.array([data_dict[k][2] for k in keys])
            rv = initialize_named_choices(keys, weights)
            # select an option and get its name and mean duration
            el_index = rv.rvs(size=1)
            key = keys[el_index]
            name = data_dict[key][0]
            dur = min(data_dict[key][1], max_time)
            dur_parts.append(dur)
            if ipart == 0:
                text = text + "    - %s" % name
            else:
                text = text + " %s" % name
    
        time = stats.poisson.rvs(min(dur_parts), size=1)
        text = text + " pour %d %s\n" % (time, unite)

    return text

if __name__ == '__main__':

    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--fich", dest="filename",
                      help="Nom fichier avec seance type et durees.",
                      action="store", type="string")
    parser.add_option("-e", "--email", dest="e_filename",
                      help="Nom fichier avec infos pour envoi email.",
                      action="store", type="string")

    (options, args) = parser.parse_args()

    step_list = read_sequence_file(options.filename)
    text = sequence(step_list)

    if options.e_filename is not None:
        send_message(options.e_filename, text, "Proposition de séance")
    else:
        print text

