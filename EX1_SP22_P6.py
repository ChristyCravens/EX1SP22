from math import *

def Simpson(fcn, a, b, npoints):
    """
    Uses the Simpson's 1/3 Rule for numerical integration to calculate the area under the curve from a to b

    :param fcn: this is the function to be integrated with Simpson's 1/3 rule
    :param a: lower limit of integration
    :param b: upper limit of integration
    :param nPoints: number of points to calculate the area under the curve
    :return: value of the area under the curve after the integration is performed
    """
    # if npoints is even add 1 to make odd.
    npoints += 1 if npoints % 2 == 0 else 0

    # Calculate step size
    h = (b - a) / (npoints - 1)
    # No coefficients of 2 or 4 for f(a) and f(b) solution
    est = fcn(a) + fcn(b)
    # Add coefficient of 4 for every other term from f(a) to f(b)
    for i in range(1, npoints, 2): est += 4 * fcn(a + (h * i))
    # Add coefficient of 2 for every other term from f(a) to f(b)
    for i in range(2, npoints - 1, 2): est += 2 * fcn(a + (h * i))
    # h/3 for Simpson's Rule & return solution
    return est * h / 3


def Secant(fcn, x0, x1, maxiter=100, xtol=1e-6):
    """
    Uses the Secant method to solve for x.
    :param fcn: the defined function for solving
    :param x0: first value of x
    :param x1: new value of x
    :param maxiter: maximum number of iterations
    :param xtol: total x values
    :return: x
    """

    # Defining parameters for use in equations
    running = True
    iter = 0
    # x1 = new value of x; x = previous value of x
    while running == True:

        # Iterate the entered number of times
        if abs(x1 - x0) <= xtol or iter > maxiter:
            running = False

        else:
            storage = x1
            x1 = x1 - fcn(x1) * ((x1 - x0) / (fcn(x1) - fcn(x0)))
            x0 = storage
            iter += 1
    # Return final solution
    return x1


def STO(Thrust):
    """
    This function calculates and returns the STO, which is the distance the airplane will roll on the runway
    before it is able to lift off into the air, by using the thrust value input by the user.
    :param Thrust: the value of the engine thrust
    :return: STO
    """
    # First, we have to enter the desired values necessary for calculations.
    Weight = 56000

    S = 1000
    Cl = 2.4
    Cd = 0.0279
    rho = 0.002377
    gc = 32.2

    # The following calculates the needed values to find STO
    A = gc * (Thrust / Weight)
    B = (gc / Weight) * (0.5 * S * rho * Cd)

    fn = lambda v: v / (A - B * v ** 2)  # Make a function to be passed to Simpson

    a = 0
    b = 1.2 * ((Weight) / (0.5 * rho * S * Cl)) ** (1 / 2)

    # Now we call the simpson function, according to our values calculated above
    STO = Simpson(fn, a, b, npoints=1000)

    # Return the STO value
    return STO

def ThrustNeededForTakeoff(distance):
    '''
    This function uses the Secant method to find the thrust needed
    for takeoff within the given distance.
    :param distance: desired takeoff distance in ft
    :return: the thrust required in lbf
    '''
    # Defining the function using lambda
    fcn=lambda t: STO(t) - distance
    # X is the new value, x is the previous value
    X = 10e3
    x = 30e3
    t = Secant(fcn, X, x) #callback for Secant
    return t

def main():
    '''
    This main calculates:
     1. the takeoff distance for a thrust of 13000 lbf
     2. thrust needed for takeoff distance of 1500 ft
     3. thrust needed for takeoff distance of 1000 ft
    :return: print statements of calculated values
    '''
    #calculate takeoff distance for thrust of 13000 lbf
    tod = STO(13000)
    #calculate thrust needed for takeoff distance of 1500 ft
    tn1 = ThrustNeededForTakeoff(1500)
    #calculate thrust needed for takeoff distance of 1000 ft
    tn2 = ThrustNeededForTakeoff(1000)
    print("Take-off distance for 13,000lb thrust = {:0.1f} ft".format(tod))
    print("Thrust needed to take off in 1,500 ft = {:0.2f} lb".format(tn1))
    print("Thrust needed to take off in 1,000 ft = {:0.2f} lb".format(tn2))

main()