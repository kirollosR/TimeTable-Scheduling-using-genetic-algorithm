from Data import Data
from Display import Display
from Population import Population

POPULATION_SIZE = 10


data = Data()
display = Display()

generationNumber = 0
print("\n> Generation # " + str(generationNumber))

# instantiating the population
population = Population(POPULATION_SIZE, data)

# sort the schedules in the population
def get_sort_key(list):
    return list.getFitness()

population.getSchedules().sort(key=get_sort_key, reverse=True)
# print generation ZERO
display.print_generation(population)

print("\n\n")
display.print_schedule_as_table(population.getSchedules()[0])