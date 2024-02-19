print("*************************************************")
print("Gasoline Branch\n\n")

# Libraries Here
import random

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel



#Function that list Gas Stations, randomly choosing one and returning its value.
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle","K","Moble","Costco","Meijer","7Eleven",""]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby

print(gasLevelGauge())
print(listOfGasStations())

