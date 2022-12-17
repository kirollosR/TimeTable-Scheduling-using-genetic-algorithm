from random import random, randint

from Population import Population
from Schedule import Schedule


class GeneticAlgorithm:
    def __init__(self, data, populationSize=10):
        self.data = data
        self.populationSize = populationSize
        self.SelectionSize = 2

    def evolve(self, population, retain=0.2, random_select=0.05, mutate=0.01):
        return self.mutation(self.crossover(population, retain), mutate, retain)
        # return self.crossover(population, retain)

    def crossover(self, population, retain):
        crossover_pop = Population(0, self.data)
        NumbOfSchedules = int(retain * self.populationSize)
        for i in range(NumbOfSchedules):
            crossover_pop.getSchedules().append(population.getSchedules()[i]) # take a copy of population list not reference
        i = NumbOfSchedules
        while i < self.populationSize:
            schedule1 = self.select_population(population).getSchedules()[0]
            schedule2 = self.select_population(population).getSchedules()[1]
            crossover_pop.getSchedules().append(self.crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule(self.data).individual()
        for i in range(0, len(crossoverSchedule.getClasses())):
            if random() > 0.5:
                crossoverSchedule.getClasses()[i] = schedule1.getClasses()[i]
            else:
                crossoverSchedule.getClasses()[i] = schedule2.getClasses()[i]
        return crossoverSchedule

    def mutation(self, population, mutate, retain):
        NumbOfSchedules = int(retain * self.populationSize)
        for i in range(NumbOfSchedules, self.populationSize):
            self.mutate_schedule(population.getSchedules()[i], mutate)
        return population

    def mutate_schedule(self, population, mutate):
        scheduler = Schedule(self.data).individual()
        # MutationRate = int(mutate * populationSize)
        for i in range(0, len(population.getClasses())):
            if mutate > random():
                population.getClasses()[i] = scheduler.getClasses()[i]
        return population

    def select_population(self, population):
        select_pop = Population(0, self.data)
        i = 0
        while i < self.SelectionSize:
            select_pop.getSchedules().append(population.getSchedules()[randint(0, self.populationSize - 1)])
            i += 1

        def get_sort_key(list):
            return list.getFitness()
        select_pop.getSchedules().sort(key=get_sort_key, reverse=True)
        # print(len(select_pop.getSchedules()))
        return select_pop
