# encoding: utf-8
from scipy import stats
import bm_prob
import bm_io
import numpy as np

email_file = 'email_jeu_TL.txt'

def make_message(noms_role, rv_role, noms_epaisseur, rv_epaisseur):
    msg = "Le jeu commence... \n\n" + \
          "Role : %s pour %d heures avec couche %s.\n" % \
               (noms_role[rv_role.rvs(size=1)],
                stats.poisson.rvs(mu_duree),
                noms_epaisseur[rv_epaisseur.rvs(size=1)])

    return msg

if __name__ == '__main__':

    noms_role = ['AB', 'DL']
    noms_epaisseur = ['jetable fine', 'jetable épaisse', 'lavable']

    mu_duree = 4

    w_role = np.array([0.25, 0.75])
    w_epaisseur = np.array([0.4, 0.4, 0.2])

    rv_role = bm_prob.initialize_named_choices(noms_role, w_role)
    rv_epaisseur = bm_prob.initialize_named_choices(noms_epaisseur, w_epaisseur)

    msg = make_message(noms_role, rv_role, noms_epaisseur, rv_epaisseur)
    bm_io.send_message(email_file, msg, 'Proposition de jeu pour TL')

    print "Proposition de jeu envoyée..."


