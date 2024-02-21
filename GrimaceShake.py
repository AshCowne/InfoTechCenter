print("*************************************************")
print("Gasoline Branch\n\n")

# Libraries Here
import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


#Function that list Gas Stations, randomly choosing one and returning its value.
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle","K","Moble","Costco","Meijer","7Eleven",""]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby

#Function will call the gasLevelGauge to determin out gas level and then
# find the closest gas station by calling the listOfGasStations function if we are on low or quarter tank.
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    print(milesToGasStationsLow)
    print(milesToGasStationsQuarterTank)
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif  gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the clossest gas station.")
        sleep(2.5)
        print("The clostest gas station is", listOfGasStations(), ",which is", milsesToGasStationsLow, "miles away.")
        
gasLevelAlert()







#print(gasLevelGauge())
#print(listOfGasStations())

