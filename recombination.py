"""
My collection of recombination methods

Student number: Ben Tomkinson
Student name: 20110965
"""

#imports
import random

def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []

    #get random position
    position = random.randint(0,len(parent1))

    #get the beginning of parent in offspring at random cut point
    offspring1[:position] = parent1[:position] 
    offspring2[:position] = parent2[:position]

    endParent1 = parent1[position:]
    endParent2 = parent2[position:]
    
    for i in endParent1:
        if i not in offspring2:
            offspring2.append(i)
    
    for i in endParent2:
        if i not in offspring1:
            offspring1.append(i)

    for i in parent1:
        if i not in offspring2:
            offspring2.append(i)

    for i in parent2:
        if i not in offspring1:
            offspring1.append(i)


    #add the parent to opposite child at the end of the cut point

    return offspring1, offspring2
#permutation_cut_and_crossfill ([7, 1, 2, 0, 6, 5, 3, 4],[3, 7, 4, 0, 5, 6, 1, 2])