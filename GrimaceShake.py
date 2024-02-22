#Import Libraries Here
import time
import sys
import random
from time import sleep


# Welcome Branch starts here,
timeToSleep = 1

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

x = 0
ellipsis = 0

while x != 20:
    x +=  1
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted Up -Retina Scanned - Access Granted!")


print("InfoTech Center Operating System Loading...")




print("*************************************************\n")
print("Gasoline Branch\n")

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
    elif  gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is a quarter tank, checking Google Maps for the clossest gas station.")
        sleep(2.5)
        print("The clostest gas station is", listOfGasStations(), ",which is", milesToGasStationsQuarterTank, "miles away.")
    elif  gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half tank that is enough for you destination.")
    elif  gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is a three quarter tank.")
    elif  gasLevelIndicator == "Full Tank":
        print("Your gas tank is full.")

gasLevelAlert()