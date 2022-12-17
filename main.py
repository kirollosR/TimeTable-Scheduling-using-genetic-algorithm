from Data import Data
from Display import Display
from GeneticAlgorithm import GeneticAlgorithm
from InputData import InputData
from Population import Population

POPULATION_SIZE = 10
retain = 0.3
random_select = 0.05
mutate = 0.1

data = InputData().getData()


# data = Data()
display = Display()

display.print_available_data(data)

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

genetic = GeneticAlgorithm(data, POPULATION_SIZE)

i = 0
while (population.getSchedules()[0].getFitness() != 1.0):
    if i != 5000:
        generationNumber += 1
        print("\n> Generation # " + str(generationNumber))
        population = genetic.evolve(population, retain, random_select, mutate)
        population.getSchedules().sort(key=get_sort_key, reverse=True)
        display.print_generation(population)
        i += 1
    else:
        break

print("\n> Final Schedules")
print("\n\n")
display.print_schedule_as_table(population.getSchedules()[0])

print("\n> IT department Schedule:")
display.printOurUsualSchedule(population.getSchedules()[0], "IT")

print("\n> IS department Schedule:")
display.printOurUsualSchedule(population.getSchedules()[0], "IS")

print("\n> CS department Schedule:")
display.printOurUsualSchedule(population.getSchedules()[0], "CS")

print("\n> General department Schedule:")
display.printOurUsualSchedule(population.getSchedules()[0], "General")

print("\n> AI department Schedule:")
display.printOurUsualSchedule(population.getSchedules()[0], "AI")
