"""
My collection of survivor selection methods

Student number: 20110965
Student name: Ben Tomkinson
"""

#imports
import random
import numpy as np

def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    # Combine the current population and offspring
    population = current_pop + offspring
    fitness = current_fitness + offspring_fitness
    
    # Rank the population based on their fitness values
    population_fitness = list(zip(population, fitness))
    population_fitness.sort(key=lambda x: x[1], reverse=True)
    
    # Select the top mu individuals from the ranked population
    new_population = [individual for individual, fit in population_fitness[:len(current_pop)]]
    new_fitness = [fit for individual, fit in population_fitness[:len(current_pop)]]
    
    return new_population, new_fitness



def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    # Combine the current population and offspring
    population = current_pop + offspring
    fitness = current_fitness + offspring_fitness
    
    # Rank the population based on their fitness values
    population_fitness = list(zip(population, fitness))
    population_fitness.sort(key=lambda x: x[1], reverse=True)
    
    #Seperate the fitness and population into seperate list
    population = [individual for individual, fit in population_fitness]
    fitness = [fit for individual, fit in population_fitness]
    
    # Replace the worst lamda current generation individuals with the lamda offspring
    new_population = population[:len(current_pop)]
    new_fitness = fitness[:len(current_pop)]
    
    return new_population, new_fitness
    

def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    # student code starts
    combined_population = np.concatenate((current_pop, offspring))
    combined_fitness = np.concatenate((current_fitness, offspring_fitness))

    selected_elements_pop = np.random.choice(combined_population, size= (len(current_pop)), replace=False)
    selected_elements_fit = np.random.choice(combined_fitness, size= (len(current_fitness)), replace=False)

    for i in selected_elements_pop:
        population.append(combined_population[i])
    
    for i in selected_elements_fit:
        fitness.append(combined_fitness[i])
        

    
    # student code ends
    
    return population, fitness

