# Problem Set 4: Simulating the Spread of Disease and Bacteria Population Dynamics
import math
import numpy as np
import pylab as pl
import random


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleBacteria
    and ResistantBacteria classes to indicate that a bacteria cell does not
    reproduce. You should use NoChildException as is; you do not need to
    modify it or add any code.
    """

def make_one_curve_plot(x_coords, y_coords, x_label, y_label, title):
    """
    Makes a plot of the x coordinates and the y coordinates with the labels
    and title provided.

    Args:
        x_coords (list of floats): x coordinates to graph
        y_coords (list of floats): y coordinates to graph
        x_label (str): label for the x-axis
        y_label (str): label for the y-axis
        title (str): title for the graph
    """
    pl.figure()
    pl.plot(x_coords, y_coords)
    pl.xlabel(x_label)
    pl.ylabel(y_label)
    pl.title(title)
    pl.show()

def make_two_curve_plot(x_coords,
                        y_coords1,
                        y_coords2,
                        y_name1,
                        y_name2,
                        x_label,
                        y_label,
                        title):
    """
    Makes a plot with two curves on it, based on the x coordinates with each of
    the set of y coordinates provided.

    Args:
        x_coords (list of floats): the x coordinates to graph
        y_coords1 (list of floats): the first set of y coordinates to graph
        y_coords2 (list of floats): the second set of y-coordinates to graph
        y_name1 (str): name describing the first y-coordinates line
        y_name2 (str): name describing the second y-coordinates line
        x_label (str): label for the x-axis
        y_label (str): label for the y-axis
        title (str): the title of the graph
    """
    pl.figure()
    pl.plot(x_coords, y_coords1, label=y_name1)
    pl.plot(x_coords, y_coords2, label=y_name2)
    pl.legend()
    pl.xlabel(x_label)
    pl.ylabel(y_label)
    pl.title(title)
    pl.show()

##########################
# PROBLEM 1
##########################

class SimpleBacteria(object):
    """A simple bacteria cell with no antibiotic resistance"""

    def __init__(self, birth_prob, death_prob):
        """
        Args:
            birth_prob (float in [0, 1]): Maximum possible reproduction
                probability
            death_prob (float in [0, 1]): Maximum death probability
        """
        self.birth_prob = birth_prob
        self.death_prob = death_prob

    def is_killed(self):
        """
        Stochastically determines whether this bacteria cell is killed in
        the patient's body at a time step, i.e. the bacteria cell dies with
        some probability equal to the death probability each time step.
        """
        return random.random() < self.death_prob

    def reproduce(self, pop_density):
        """
        Stochastically determines whether this bacteria cell reproduces at a
        time step. The bacteria cell reproduces with probability
        self.birth_prob * (1 - pop_density).

        Args:
            pop_density (float): The population density, defined as the
                current bacteria population divided by the maximum population

        Returns:
            SimpleBacteria: A new instance representing the offspring of
                this bacteria cell (if the bacteria reproduces). The child
                should have the same birth_prob and death_prob values as
                this bacteria.

        Raises:
            NoChildException if this bacteria cell does not reproduce.
        """
        if random.random() < self.birth_prob * (1 - pop_density):
            return SimpleBacteria(self.birth_prob, self.death_prob)
        raise NoChildException

class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any
    antibiotics and his/her bacteria populations have no antibiotic resistance.
    """
    def __init__(self, bacteria, max_pop):
        """
        Args:
            bacteria (list of SimpleBacteria): The bacteria in the population
            max_pop (int): Maximum possible bacteria population size for
                this patient
        """
        self.bacteria = bacteria
        self.max_pop = max_pop

    def get_total_pop(self):
        """
        Gets the size of the current total bacteria population.
        """
        return len(self.bacteria)

    def update(self):
        """
        Update the state of the bacteria population in this patient for a
        single time step.

        Returns:
            int: The total bacteria population at the end of the update
        """
        # Determine who survives
        surviving_cells = list(filter(lambda x: not x.is_killed(), self.bacteria))
        # Calc pop density
        pop_density = len(surviving_cells) / self.max_pop
        self.bacteria = []
        for bacteria in surviving_cells:
            self.bacteria.append(bacteria)
            try:
                self.bacteria.append(bacteria.reproduce(pop_density))
            except:
                continue
        return self.get_total_pop()

##########################
# PROBLEM 2
##########################

def calc_pop_avg(populations, n):
    """
    Finds the average bacteria population size across trials at time step n

    Args:
        populations (list of lists or 2D array): populations[i][j] is the
            number of bacteria in trial i at time step j

    Returns:
        float: The average bacteria population size at time step n
    """
    total = 0
    for trial in populations:
        total += trial[n]
    return total / len(populations)

def simulation_without_antibiotic(num_bacteria,
                                  max_pop,
                                  birth_prob,
                                  death_prob,
                                  num_trials):
    """
    Run the simulation and plot the graph for problem 2. No antibiotics
    are used, and bacteria do not have any antibiotic resistance.

    For each of num_trials trials:
        * simulate changes to the bacteria population for 300 timesteps,
          recording the bacteria population after each time step. Note
          that the first time step should contain the starting number of
          bacteria in the patient

    Args:
        num_bacteria (int): number of SimpleBacteria to create for patient
        max_pop (int): maximum bacteria population for patient
        birth_prob (float in [0, 1]): maximum reproduction
            probability
        death_prob (float in [0, 1]): maximum death probability
        num_trials (int): number of simulation runs to execute

    Returns:
        populations (list of lists or 2D array): populations[i][j] is the
            number of bacteria in trial i at time step j
    """
    populations = []
    for trial in range(num_trials):
        populations.append([])
        bacteria = [SimpleBacteria(birth_prob, death_prob) for _ in range(num_bacteria)]
        patient = Patient(bacteria, max_pop)
        for time in range(300):
            pop = patient.update()
            populations[-1].append(pop)
    return populations

# When you are ready to run the simulation, uncomment the next line
# populations = simulation_without_antibiotic(100, 1000, 0.1, 0.025, 20)
# y = [calc_pop_avg(populations, i) for i in range(300)]
# x = list(range(300))
# make_one_curve_plot(x, y, 'Time (generation)', 'Population', 'Population at Time t')

##########################
# PROBLEM 3
##########################
def calc_pop_std(populations, t):
    """
    Finds the standard deviation of populations across different trials
    at time step t.
        * compute average squared distance of the data points from the average
          and take its square root

    Args:
        populations (list of lists or 2D array): populations[i][j] is the
            number of bacteria present in trial i at time step j
        t (int): time step

    Returns:
        float: the standard deviation of populations across different trials at
             a specific time step
    """
    values_at_time_t = [k[t] for k in populations]
    average = sum(values_at_time_t) / len(values_at_time_t)
    return (sum([(i - average)**2 for i in values_at_time_t]) / len(values_at_time_t))**.5

def calc_95_ci(populations, t):
    """
    Finds a 95% confidence interval around the average bacteria population
    at time t

    Args:
        populations (list of lists or 2D array): populations[i][j] is the
            number of bacteria present in trial i at time step j
        t (int): time step

    Returns:
        mean (float): the sample mean
        width (float): 1.96 * SEM
    """
    sem = calc_pop_std(populations, t) / (len(populations) ** 0.5)
    return (calc_pop_avg(populations, t), 1.96 * sem)

##########################
# PROBLEM 4
##########################

class ResistantBacteria(SimpleBacteria):
    """A bacteria cell that can have antibiotic resistance."""

    def __init__(self, birth_prob, death_prob, resistant, mut_prob):
        """
        Args:
            birth_prob (float in [0, 1]): reproduction probability
            death_prob (float in [0, 1]): death probability
            resistant (bool): whether this bacteria has antibiotic resistance
            mut_prob (float): mutation probability for this
                bacteria cell. This is the maximum probability of the
                offspring acquiring antibiotic resistance
        """
        super().__init__(birth_prob, death_prob)
        self.resistant = resistant
        self.mut_prob = mut_prob

    def get_resistant(self):
        """Returns whether the bacteria has antibiotic resistance"""
        return self.resistant

    def is_killed(self):
        """Stochastically determines whether this bacteria cell is killed in
        the patient's body at a given time step.
        """
        if self.get_resistant():
            return random.random() < self.death_prob
        return random.random() < self.death_prob / 4

    def reproduce(self, pop_density):
        """
        Stochastically determines whether this bacteria cell reproduces at a
        time step.

        Args:
            pop_density (float): the population density

        Returns:
            ResistantBacteria: an instance representing the offspring of
            this bacteria cell (if the bacteria reproduces). The child should
            have the same birth_prob, death_prob values and mut_prob
            as this bacteria.
        """
        if random.random() < self.birth_prob * (1 - pop_density):
            resistance = True
            if not self.get_resistant():
                if not random.random() < self.mut_prob * (1 - pop_density):
                    resistance = False
            return ResistantBacteria(self.birth_prob, self.death_prob, resistance, self.mut_prob)
        raise NoChildException

class TreatedPatient(Patient):
    """
    Representation of a treated patient. The patient is able to take an
    antibiotic and his/her bacteria population can acquire antibiotic
    resistance. The patient cannot go off an antibiotic once on it.
    """
    def __init__(self, bacteria, max_pop):
        """
        Args:
            bacteria: The list representing the bacteria population (a list of
                      bacteria instances)
            max_pop: The maximum bacteria population for this patient (int)
        """
        super().__init__(bacteria, max_pop)
        self.on_antibiotic = False

    def set_on_antibiotic(self):
        """
        Administer an antibiotic to this patient. The antibiotic acts on the
        bacteria population for all subsequent time steps.
        """
        self.on_antibiotic = True

    def get_resist_pop(self):
        """
        Get the population size of bacteria cells with antibiotic resistance
        """
        return len([b for b in self.bacteria if b.get_resistant()])

    def update(self):
        """
        Update the state of the bacteria population in this patient for a
        single time step.

        Returns:
            int: The total bacteria population at the end of the update
        """
        survivors = list(filter(lambda x: not x.is_killed(), self.bacteria))
        if self.on_antibiotic:
            survivors = list(filter(lambda x: x.get_resistant(), survivors))
        pop_density = len(survivors) / self.max_pop
        self.bacteria = []
        for bacteria in survivors:
            self.bacteria.append(bacteria)
            try:
                self.bacteria.append(bacteria.reproduce(pop_density))
            except:
                continue
        return self.get_total_pop()

##########################
# PROBLEM 5
##########################

def simulation_with_antibiotic(num_bacteria,
                               max_pop,
                               birth_prob,
                               death_prob,
                               resistant,
                               mut_prob,
                               num_trials):
    """
    For each of num_trials trials:
        * run a simulation for 150 timesteps, add the antibiotic, and run the
          simulation for an additional 250 timesteps, recording the total
          bacteria population and the resistance bacteria population after
          each time step

    Plot the average bacteria population size for both the total bacteria
    population and the antibiotic-resistant bacteria population (y-axis) as a
    function of elapsed time steps (x-axis) on the same plot. You might find
    the helper function make_two_curve_plot helpful

    Returns: a tuple of two lists of lists, or two 2D arrays
        populations (list of lists or 2D array): the total number of bacteria
            at each time step for each trial; total_population[i][j] is the
            total population for trial i at time step j
        resistant_pop (list of lists or 2D array): the total number of
            resistant bacteria at each time step for each trial;
            resistant_pop[i][j] is the number of resistant bacteria for
            trial i at time step j
    """
    populations = []
    resistant_pop = []
    for trial in range(num_trials):
        populations.append([])
        resistant_pop.append([])
        bacteria = [ResistantBacteria(birth_prob, death_prob, resistant, mut_prob) for _ in range(num_bacteria)]
        patient = TreatedPatient(bacteria, max_pop)
        for tick in range(400):
            if tick == 150: patient.set_on_antibiotic()
            pop = patient.update()
            populations[-1].append(pop)
            resistant_pop[-1].append(patient.get_resist_pop())
    return (populations, resistant_pop)

# total_pop, resistant_pop = simulation_with_antibiotic(num_bacteria=100,
#                                                       max_pop=1000,
#                                                       birth_prob=0.3,
#                                                       death_prob=0.2,
#                                                       resistant=False,
#                                                       mut_prob=0.8,
#                                                       num_trials=10)

total_pop, resistant_pop = simulation_with_antibiotic(num_bacteria=100,
                                                      max_pop=1000,
                                                      birth_prob=0.17,
                                                      death_prob=0.2,
                                                      resistant=False,
                                                      mut_prob=0.8,
                                                      num_trials=50)
y1 = [calc_pop_avg(total_pop, i) for i in range(len(total_pop[0]))]
x1 = list(range(400))
y2 = [calc_pop_avg(resistant_pop, i) for i in range(len(resistant_pop[0]))]
x2 = list(range(400))
make_two_curve_plot(x1, y1, y2, 'y1', 'y2', 'xla', 'yla', 'title')
