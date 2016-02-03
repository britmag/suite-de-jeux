# encoding: utf-8
from scipy import stats
from random import shuffle
from bm_io import read_data_file, send_message

def training_times(data_dict, max_time):
    """
    Crée un programme d'entrainement sur la base des éléments choisis 
    et un temps maximum.
    """
    elements = data_dict.values()
    shuffle(elements)
    time_left = max_time

    text =  "\nEntrainement sur %d minutes : \n" % max_time
    for el in elements:
        name = el[0]
        time = stats.poisson.rvs(el[1], size=1)
        if time >= time_left:
            continue
        else:
            time_left = time_left - time
            text = text +  "  - %s : %d minutes\n" % (name, time)

    return text

if __name__ == '__main__':

    duree = 15
    data_dict = read_data_file('positions_britmag.txt')
    text = training_times(data_dict, duree)

    duree = 45
    data_dict = read_data_file('accessoires_britmag.txt')
    text = text + training_times(data_dict, duree)

    send_message('email_entrainement.txt', text, "Séquence d'entrainement")

