"""
My collection of parent selection methods

Student number: Ben Tomkinson
Student name: 20110965
"""

# imports
import random


def MPS(fitness, mating_pool_size):
    selected_to_mate = []
    #This calculates of the summation of the total fitness for the entire population
    fitness_sum = sum(fitness)

    #for amount of parents to be selected
    for i in range(mating_pool_size):

        #Selects a random number found in the fitness sum
        rand = random.uniform(0, fitness_sum)

        #goes over until the highest fitness is found, does this by decrementing until its below zero
        for j in range(len(fitness)):
            rand -= fitness[j]
            if rand <= 0:
                selected_to_mate.append(j)
                fitness_sum -= fitness[j]
                break
   
    return selected_to_mate



def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    population_size = len(fitness)
    selected_to_mate = []
    for i in range(mating_pool_size):

        #Randomly select parents from the tournament_size
        tournament_indices = random.sample(range(population_size), tournament_size)

        #Choose the one with the highest fitness value, start with the first one then iterate over rest
        best_index = tournament_indices[0]

        #Used to iterate over the rest of the selected population
        rest_of_tournament = tournament_indices[1:]
        for j in rest_of_tournament:

            #Replaces the best_index value with the highest fitnes found
            if fitness[j] > fitness[best_index]:
                best_index = j

        selected_to_mate.append(best_index)
    
    return selected_to_mate


def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = []
    
    #Select the number of mating_pool size individuals that are non-repeating
    selected_to_mate = random.sample(range(population_size), mating_pool_size)
    return selected_to_mate
    
    
