from typing import List
import random

def binary_search(cities: List[str], city: str) -> int:
    left = 0
    right = len(cities) - 1

    while left <= right:
        middle = (right + left) // 2
        if cities[middle] > city:
            right = middle -1
        else:
            left = middle + 1
    return left

def max_cities(cities: List[str], distances: List[int]) -> int:
    # Step I: Create a map of distances and corresponding cities, and sort the cities by their distances, to make this a Longest-Increasing-Subsequence problem, except for using alphebet comparison than numbers.
    us_map = {}
    for i in range(len(cities)):
        city = cities[i]
        distance = distances[i]
        if city not in us_map:
            us_map[distance] = city

    
    # print(dict(sorted(us_map.items())))
    us_map = dict(sorted(us_map.items()))
    ordered_cities = list(us_map.values())
    print("Cities ordered by distance:")
    print(ordered_cities)

    # Step II: solve like a Longest-Increasing-Subsequence problem
    plan = []
    for city in ordered_cities:
        if not plan or city > plan[-1]:
            plan.append(city)
        else:
            i = binary_search(plan, city)
            plan[i] = city
            
    print("List after greedy propagation + binary search, each representing the smallest end city name:")
    print(plan)
    return(len(plan))
        





if __name__ == "__main__":
    # Test Case 1: ~10 U.S. cities
    cities_10 = [
        "Seattle", "San Francisco", "Los Angeles", "Las Vegas", "Denver",
        "Chicago", "Houston", "Atlanta", "Washington", "New York"
    ]
    distances_10 = [0, 50, 100, 200, 400, 600, 800, 900, 1000, 1100]  # Approximate “west to east” scale
    combined_10 = list(zip(distances_10, cities_10))
    random.shuffle(combined_10)
    d10, c10 = zip(*combined_10)

    print("Test 1 Result:", max_cities(list(c10), list(d10)))

    # Test Case 2: 50 U.S. cities
    cities_50 = [
        "Seattle", "Portland", "San Francisco", "Los Angeles", "San Diego", "Las Vegas", "Phoenix", "Tucson",
        "Salt Lake City", "Boise", "Denver", "Albuquerque", "El Paso", "Dallas", "Austin", "Houston",
        "Oklahoma City", "Kansas City", "Minneapolis", "Omaha", "St. Louis", "Chicago", "Indianapolis",
        "Cleveland", "Detroit", "Columbus", "Pittsburgh", "Philadelphia", "Baltimore", "Washington",
        "Charlotte", "Atlanta", "Orlando", "Miami", "Tampa", "Nashville", "Louisville", "Cincinnati",
        "New Orleans", "Memphis", "Birmingham", "Raleigh", "Richmond", "Norfolk", "Boston", "New York",
        "Buffalo", "Albany", "Providence", "Hartford"
    ]
    distances_50 = list(range(0, 5000, 100))[:50]  # Simplified distance scale (west to east)
    combined_50 = list(zip(distances_50, cities_50))
    random.shuffle(combined_50)
    d50, c50 = zip(*combined_50)

    print("Test 2 Result:", max_cities(list(c50), list(d50)))
