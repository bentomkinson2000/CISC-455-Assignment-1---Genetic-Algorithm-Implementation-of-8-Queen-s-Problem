"""
My collection of initialization methods for different representations

Student number: 20110965
Student name: Ben Tomkinson
"""

#imports
import numpy as np

def permutation (pop_size, chrom_length):
    """initialize a population of permutation"""

    population = []
    # student code begin
    for i in range(pop_size):
        population.append(np.random.choice(range(chrom_length), chrom_length, replace=False))
    #student code end
    
    return population       
print(permutation(10,8))              
