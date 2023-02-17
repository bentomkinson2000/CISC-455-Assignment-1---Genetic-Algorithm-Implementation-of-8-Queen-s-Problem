"""
My colleciton of mutation methods

Student number: 20110965
Student name: Ben Tomkinson
"""

# imports
import random

def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    
    # student code starts
    pos = random.sample(range(0,8),2)
    mutant[pos[0]] = individual[pos[1]]
    mutant[pos[1]] = individual[pos[0]]
   
    # student code ends
  
    return mutant

