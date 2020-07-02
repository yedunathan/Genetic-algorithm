#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
random.seed(1234)
def generate_Random_Population(nq):
    random_pop  = [random.randint(1,8) for _ in range(8)]                                
    return random_pop

def fitness(unique_Identity):
    sum_queens = [unique_Identity.count(queen)-1 for queen in unique_Identity]
    horizontal_collisions = sum(sum_queens)/2
    diagonal_collisions = 0
   
    n = len(unique_Identity)

    left_diagonal = [0] * 2*n

    right_diagonal = [0] * 2*n
   
    for i in range(n):
       
        left_index = i + unique_Identity[i] - 1
        right_index = len(unique_Identity) - i + unique_Identity[i] - 2
       
        left_diagonal[left_index] += 1
        right_diagonal[right_index] += 1
     
    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
       
        if left_diagonal[i] > 1:
           
            counter += left_diagonal[i]-1
           
               
       
        if right_diagonal[i] > 1:
           
            counter += right_diagonal[i]-1
           
        diagonal_collisions += counter / (n-abs(i-n+1))

    score = int(maxFitness - (horizontal_collisions + diagonal_collisions))

    return score
def probability(unique_Identity, fitness):
    probability = fitness(unique_Identity) / maxFitness
    return probability

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
       
def reproduce(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    reproduced_population = x[0:c] + y[c:n]
    return reproduced_population

def mutate(x):
    c = random.randint(0,  len(x) - 1)
    m = random.randint(1,  len(x))
    x[c] = m
    return x

def next_Generation(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities)
        y = random_pick(population, probabilities)
        child = reproduce(x, y)
        if random.random() < mutation_probability:
            child = mutate(child)
        print_unique_Identity(child)
        new_population.append(child)
        if fitness(child) == maxFitness:
            break
    return new_population

def print_unique_Identity(chrom):
    new_list = []
    new_list = [x-1 for x in chrom]
    #print(new_list)

    print("{},  Fitness = {}"
        .format(str(new_list), fitness(chrom)))




if __name__ == "__main__":
    nq = 8
    maxFitness = (nq*(nq-1))/2
    population = [generate_Random_Population(nq) for _ in range(100)]
   
    generation = 1

    while not maxFitness in [fitness(chrom) for chrom in population]:
        print("=== Generation {} ===".format(generation))
        population = next_Generation(population, fitness)
        print("")
        print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1
    chrom_out = []
    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("");
            print("Output: ")
            chrom_out = chrom
            print_unique_Identity(chrom)


# In[ ]:





# In[ ]:




