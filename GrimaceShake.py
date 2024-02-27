print("Weather***********************************")

print("Weather Branch\n")

#Inport Libraries Here
import random
from time import sleep

#Created a function that randomly chooses the weather from the list
def weather():
    weatherForcast = ["snowy", "blizzard", "rainy", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForcast)
    return weatherConditions

#Variable to call the weather() once VRS(Vehicle Response System) is determined

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forcast of", weatherAlert,"weather conditions.")
        sleep(2)
        print("VRS has bean engaged only allowing you to drive 50mph.")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forcast of", weatherAlert,"weather conditions.")
        sleep(2)
        print("VRS has bean engaged only allowing you to drive 40mph.")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forcast of", weatherAlert,"weather conditions.")
        sleep(2)
        print("VRS has bean engaged only allowing you to drive 60mph.")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forcast of", weatherAlert,"weather conditions.")
        sleep(2)
        print("VRS has bean engaged only allowing you to drive 30mph.")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 50 minutes because of the forcast of", weatherAlert,"weather conditions.")
        sleep(2)
        print("VRS has bean engaged only allowing you to drive 50mph.")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 50 minutes because of the forcast of", weatherAlert,"weather conditions.")
        sleep(2)
        print("VRS has bean engaged only allowing you to drive 20mph.")
    else:
        print("\nNational Weather Service forecasts", weatherAlert, "weather conditions")
        print("VRS has been disengaged! Drive")

