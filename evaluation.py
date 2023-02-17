"""
My collection of fitness evaluation methods

Student number: 20110965
Student name: Ben Tomkinson
"""

#imports
import numpy as np



def fitness_8queen (individual): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    
    matrix = np.zeros((8,8))
    for i in range(len(individual)):
      matrix[individual[i]][i] = 1

    x_cord = 0
    individual_cord = []
    for geno in individual:
      individual_cord.append((x_cord, geno))
      x_cord +=1
    
    total_score = 0
    for i in individual_cord:
      total_score += collision(i, individual_cord)

    return (28 - total_score)



def collision(point, cords):
    score = 0
    for i in range(8):
      for j in range(8):
        test_point = (i,j)
        if test_point in cords:
          #change in x from given point
          dx = abs(point[0] - i)
          #change in y from given point
          dy = abs(point[1] - j)
          #a difference of 0 between points means they are diagnol to each other
          if abs(dx - dy) == 0:
            score +=1
      
    return score - 1
    


  




  
 
  

#fitness_8queen([6, 3, 7, 0, 5, 3, 1, 4])

