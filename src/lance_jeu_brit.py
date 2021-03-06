# encoding: utf-8
from scipy import stats
import bm_prob
import bm_io
import numpy as np

email_file = 'email_jeu_britmag.txt'

def make_message(noms_att, rv_att, noms_instrum, rv_instrum, noms_acc, rv_acc):
    msg = "Le jeu commence... \n\n" + \
          "Position d'attente : %s pour %d minutes avec %s.\n" % \
               (noms_att[rv_att.rvs(size=1)],
                stats.poisson.rvs(mu_att),
                noms_acc[rv_acc.rvs(size=1)]) + \
          "Traitement : %s, %d fois (ou minutes),\n" % \
               (noms_instrum[rv_instrum.rvs(size=1)],
                stats.poisson.rvs(mu_instrum)) + \
          "             zone à cibler et dureté selon appréciation."


    return msg

if __name__ == '__main__':

    noms_att = ['couchée', 'débout', 'assise', 'à genou']
    noms_instrum = ['fessée à la main',
                'fessée à la brosse',
                'fessée à la cravache',
                'fessée à la canne anglaise',
                'fessée avec la latte',
                'stimulation à la roulette',
                'stimulation au vibro']
    noms_acc = ['rien', 'pinces aux seins', 'culotte en string', 'plug']

    mu_att = 10
    mu_instrum = 15

    w_att = bm_prob.setup_uniform_weights(noms_att)
    w_instrum = bm_prob.setup_ordered_weights(noms_instrum)
    w_acc = bm_prob.setup_ordered_weights(noms_acc)

    rv_att = bm_prob.initialize_named_choices(noms_att, w_att)
    rv_instrum = bm_prob.initialize_named_choices(noms_instrum, w_instrum)
    rv_acc = bm_prob.initialize_named_choices(noms_acc, w_acc)

    msg = make_message(noms_att, rv_att, noms_instrum, rv_instrum, noms_acc, rv_acc)
    bm_io.send_message(email_file, msg, "Proposition de jeu pour Britannie")

    print "Proposition de jeu envoyée..."


