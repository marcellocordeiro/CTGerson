import math

class car:
    def __init__(self, carId, latitude, longitude):
        self.carId = carId
        self.latitude = latitude
        self.longitude = longitude

def getKey(key):
    return key[1]

def calculateDistances(busPosition, policeCarPositions):
    distances = []
    
    for car in policeCarPositions:
        distances.append((car.carId, math.sqrt((busPosition.latitude - car.latitude) ** 2 + (busPosition.longitude - car.longitude) ** 2)))
    
    distances.sort(key = getKey)

    print(distances)

    return distances

def main():
    test = []
    test.append(car(0, 0, 0))
    test.append(car(1, 1, 1))
    test.append(car(2, 3, 3))

    distances = calculateDistances(car(3, 100, 100), test)

if __name__ == "__main__":
    main()
