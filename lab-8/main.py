import csv
import random


def shortest_distance(cities, distances):
    distance_traveled = 0
    current_city = random.choice(cities)
    visited = []
    visited.append(current_city)
    while len(visited) < len(cities):
        nearest_city = random.choice([city for city in cities if city not in visited])
        for city in cities:
            if city not in visited:
                if distances[current_city][city] < distances[current_city][nearest_city]:
                        nearest_city = city
        distance_traveled += distances[current_city][nearest_city]
        visited.append(nearest_city)
        current_city = nearest_city
    return distance_traveled, visited


def from_csv(country):
    with open(country, newline='') as csvfile:
        table = list(csv.reader(csvfile, delimiter=','))
        cities = table[0][1:]
        distances = {}
        for i, city in enumerate(cities):
            distances[city] = {}
            for j, distance in enumerate(table[i + 1][1:]):
                distances[city][cities[j]] = int(distance) if distance else None
    return cities, distances


if __name__ == '__main__':
    cities, distances = from_csv("france.csv")
    print("Список міст: " + ', '.join(cities))
    distance, visited = shortest_distance(cities, distances)
    print("Знайдена відстань: " + str(distance))
    print("Подорож: " + ' → '.join(visited))
