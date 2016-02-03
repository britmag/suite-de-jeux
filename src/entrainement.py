# encoding: utf-8
from scipy import stats
from random import shuffle
from bm_io import read_data_file

def training_times(data_dict, max_time):
    """
    Crée un programme d'entrainement sur la base des éléments choisis 
    et un temps maximum.
    """
    elements = data_dict.values()
    shuffle(elements)
    time_left = max_time

    print "Entrainement sur %d minutes : " % max_time
    for el in elements:
        name = el[0]
        time = stats.poisson.rvs(el[1], size=1)
        if time >= time_left:
            continue
        else:
            time_left = time_left - time
            print "  - %s : %d minutes" % (name, time)

    print "Bon travail !!"

if __name__ == '__main__':

    duree = 120

    data_dict = read_data_file('accessoires_britmag.txt')
    training_times(data_dict, duree)

    data_dict = read_data_file('positions_britmag.txt')
    training_times(data_dict, duree)

