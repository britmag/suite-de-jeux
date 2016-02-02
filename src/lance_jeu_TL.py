# encoding: utf-8
from scipy import stats
import bm_prob
import numpy as np
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def make_message(noms_role, rv_role, noms_epaisseur, rv_epaisseur):
    msg = "Le jeu commence... \n\n" + \
          "Role : %s pour %d heures avec couche %s.\n" % \
               (noms_role[rv_role.rvs(size=1)],
                stats.poisson.rvs(mu_duree),
                noms_epaisseur[rv_epaisseur.rvs(size=1)])


    return msg

def send_message(body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    fromaddr = "FROMADD@gmail.com"
    toaddr = "TOADD@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Proposition de jeu"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()

    server.starttls()
    server.login(fromaddr, PASSWORD)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

if __name__ == '__main__':

    noms_role = ['AB', 'DL']
    noms_epaisseur = ['jetable fine', 'jetable épaisse', 'lavable']

    mu_duree = 4

    w_role = np.array([0.25, 0.75])
    w_epaisseur = np.array([0.4, 0.4, 0.2])

    rv_role = bm_prob.initialize_named_choices(noms_role, w_role)
    rv_epaisseur = bm_prob.initialize_named_choices(noms_epaisseur, w_epaisseur)

    msg = make_message(noms_role, rv_role, noms_epaisseur, rv_epaisseur)
    send_message(msg)

    print "Proposition de jeu envoyée..."


