# rosalind_indepent_alleles
Calculates genotype probability

This program solves the Independent Alleles (ID - LIA) problem on the bioinformatics website Rosalind.
It finds the probability that at least a certain number of individuals (k) will possess the genotype AaBb in a given generation (n).

Inputs are n - the number of generations from the 0th generation, and k - the minimum number of individuals in generation n that have the genotype AaBb.
Output is the probability that at least k individuals are AaBb in the nth generation, found by binomial probability.
