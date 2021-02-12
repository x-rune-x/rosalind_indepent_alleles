import scipy as ss
from scipy.stats import binom

def calc_AaBb_prob(n, k):

    # Parameters of problem specify each member of the current generation gives birth to 2 new members.
    # With this we can find the number of members in the nth generation.
    gen_pop = 2**n
    # The problem asks to calculate the probability that at least as many members as k have the AaBb genotype.
    # We need to find a list of exact outcomes between k and the total population.
    r_list = list(range(k, gen_pop + 1))

    total_prob = 0
    # To find the probability of at least as many as k we need to sum the exact probabilities of outcomes between k
    # and gen_pop.
    for r in r_list:
        # Because each member always pairs with an AaBb mate,
        # the probability of their offspring being AaBb is always 25%.
        total_prob += ss.stats.binom.pmf(r, gen_pop, 0.25)

    return total_prob


solution = calc_AaBb_prob(6, 15)
print(solution)
