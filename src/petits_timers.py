from scipy import stats
from random import shuffle

def run_timers(names, mu):
    shuffle(names)
    times = stats.poisson.rvs(mu, size=len(names))

    for it in xrange(len(times)):
        print "%s : %d minutes" % (names[it], times[it])

    print "Total = %d minutes\n" % sum(times)


if __name__ == '__main__':
    #court
    names_court = ['Pince levre', 'Pince sein gauche', 'Pince sein droit',
                   'Contention seins', 'Slip avec elastique']
    names_long = ['Slip string coton', 'Maintien posture']

    run_timers(names_court, 12)

    run_timers(names_long, 45)

