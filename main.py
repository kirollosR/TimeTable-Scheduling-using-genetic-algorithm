from Data import Data
from Display import Display
from Population import Population

POPULATION_SIZE = 10


data = Data()
display = Display()

generationNumber = 0
print("\n> Generation # " + str(generationNumber))

population = Population(POPULATION_SIZE, data)

def get_sort_key(list):
    return list.getFitness()

population.getSchedules().sort(key=get_sort_key, reverse=True)
display.print_generation(population)
