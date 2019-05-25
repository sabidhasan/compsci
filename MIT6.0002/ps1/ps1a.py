# 6.0002 Problem Set 1a: Space Cows 
from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    ret = {}
    with open(filename) as f:
        for line in f.readlines():
            name, weight = line.strip().split(',')
            ret[name] = int(weight)
    return ret

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows.

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)

    trips = []
    picked_cows = set()
    while len(picked_cows) != len(sorted_cows):
        # Pick heaviest cow possible
        weight_left_curr_trip = limit
        curr_trip = []
        for (i, cow) in enumerate(sorted_cows):
            if not i in picked_cows and cow[1] <= weight_left_curr_trip:
                picked_cows.add(i)
                curr_trip.append(cow[0])
                weight_left_curr_trip -= cow[1]
        trips.append(curr_trip)
    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    best_trip = None
    # Loop through all possible partitions of cows
    for partition in get_partitions(cows.items()):
        # Check if this solution is valid (meets limit)
        if all(sum(cow[1] for cow in trip) <= limit for trip in partition):
            if best_trip is None or len(best_trip) > len(partition):
                best_trip = [[cow[0] for cow in trip] for trip in partition]
    return best_trip
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass



cows = load_cows('ps1_cow_data.txt')
# print(cows)
print(greedy_cow_transport(cows))
print(brute_force_cow_transport(cows))
