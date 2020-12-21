import random

#return true if list is sorted
def isSorted(celestialBodies):
    return celestialBodies == sorted(celestialBodies)

#veryEfficiently sort list alphabetically
def bogosort(celestialBodies):
    while not isSorted(celestialBodies):
        random.shuffle(celestialBodies)
        print(celestialBodies)
    return celestialBodies

print("Is my horoscope true?")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune","Pluto"]
random.shuffle(planets)
bogosort(planets)
print(planets)
print("THE PLANETS ARE ALPHABETICALLY ALIGNED. Your horoscope must be true.")