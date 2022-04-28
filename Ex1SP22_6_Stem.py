from math import *
from hw2a import Simpson
from hw2b import Secant

def STO(thrust):
    pass

def ThrustNeededForTakeoff(distance):
    '''
    This function uses the Secant method to find the thrust needed
    for takeoff within the given distance.
    :param distance: desired takeoff distance in ft
    :return: the thrust required in lbf
    '''
    fn=lambda t: #$JES Missing Code$ #callback for Secant
    thrust=#$JES Missing Code$  #calculate the thrust
    return thrust

def main():
    '''
    This main calculates:
     1. the takeoff distance for a thrust of 13000 lbf
     2. thrust needed for takeoff distance of 1500 ft
     3. thrust needed for takeoff distance of 1000 ft
    :return:
    '''
    #calculate takeoff distance for thrust of 13000 lbf
    tod=#$JES Missing Code$
    #calculate thrust needed for takeoff distance of 1500 ft
    tn1=#$JES Missing Code$
    #calculate thrust needed for takeoff distance of 1000 ft
    tn2=#$JES Missing Code$
    print("Take-off distance for 13,000lb thrust = {:0.1f} ft".format(tod))
    print("Thrust needed to take off in 1,500 ft = {:0.2f} lb".format(tn1))
    print("Thrust needed to take off in 1,000 ft = {:0.2f} lb".format(tn2))

main()