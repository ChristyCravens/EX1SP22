from math import *

def GetRandInt(seeds):
    """
    This program uses the Wichmann-Hill algorithm to find random integers for seeds.
    :param s1: seed value 1 to be stored in the tuple
    :param s2: seed value 2 to be stored in the tuple
    :param s3: seed value 3 to be stored in the tuple
    :return: r, s1, s2, s3
    """
    # Wichmann-Hill algorithm
    s1, s2, s3=seeds
    s1 = (171 * s1) % 30269
    s2 = (172 * s2) % 30307
    s3 = (170 * s3) % 30323
    r = ((s1 / 30269.0) + (s2 / 30307.0) + (s3 / 30232.0)) % 1
    return r, [s1, s2, s3]

def Simpson(fcn, args, a, c, nPoints=1000):
    """Uses the Simpson's 1/3 Rule for numerical integration to calculate the area under the curve from a to b

    :param fcn: this is the function to be integrated with Simpson's 1/3 rule
    :param args: tuple containing to pass to fcn
    :param a: lower limit of integration
    :param c: upper limit of integration, also equal to b
    :param nPoints: number of points to calculate the area under the curve
    :return: value of the area under the curve after the integration is performed
    """
    # Redefine a and b, then calculate the value for h
    a = args[0] - args[1]*5
    b = c
    h = (b-a)/nPoints

    # List for the values for x
    x = list()
    # List for the values for f(x)
    fx = list()
    # "I" keeps track of the loop iterations until it reaches nPoints
    I = 0
    # Loop the program until all iterations are completed
    while I <= nPoints:
        x.append(a+I*h)
        fx.append(fcn(x[I], args))
        I += 1

    # Create a list to store resulting values, as well as establishing the iterations counter again
    result = 0
    I = 0
    # Loop to determine resulting values until nPoints is reached, while organizing said values
    while I <= nPoints:
        if I == 0 or I == nPoints:
            result += fx[I]
        elif I % 2 != 0:
            result += 4*fx[I]
        else:
            result += 2*fx[I]

        I += 1
    result = result*(h/3)
    return result

def GNPDF(x, args):
    """
    Uses the Gaussian Normal Probability Density Function, about the population mean (m) and
    the population standard deviation (s).

    :param x: value used in comparison with c for the probability
    :param args: mean, standard deviation
    :return: f(x) as fcn
    """

    # Unpack args first
    m,s = args
    # Create the function (Fn) for the GNPDF and return the resultant
    fcn = (1/(s*sqrt(2*pi))) * exp(-0.5*((x-m)/s)**2)
    return fcn

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
    # x1 = new value of x; x0 = previous value of x
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

def Clamp(x, fLow, fHigh):
    """
    This function clamps a number between fLow and fHigh, inclusive
    :param x: the number to be clamped
    :param fLow: the low value for the range
    :param fHigh: the high value for the range
    :return: the clamped value and a boolean if the number got clamped
    """
    if x>fHigh: return fHigh,True
    if x<fLow: return fLow, True
    return x,False

def Variance(x, nums):
    """
    This function finds the variance for a value in a given list of numbers.
    :param x: values
    :param nums: given list of numbers
    :return:
    """
    # Set initial value of y to 0 so it starts counting at 1
    y=0
    # For loop that will sum the values of x
    for i in range(len(nums)):
        y = y + nums[i]
    # Returns the new values for y
    return y

def main():
    '''
    This main creates a list of uniformly, randomly distributed probabilities and finds corresponding
    values of x by integrating GNPDF between mu-5*sigma to x.
    step 1. Create seeds, mu, sigma, LowLim values
    step 2. Calculate pMin as lower limit on probabilities.
    step 3. create a lambda of p-P(x<c|N(mu,sigma)), such that picking correct c sets lambda fn to zero
    step 4. build list of random p values and use Secant method to find corresponding x.
    step 5. output lists of p and x along with estimates for mu, var, sigma for population
    :return: no return value
    '''
    #step 1.
    seeds= [1234, 19857, 25000] #initial seed values for the pseudorandom number generator
    mu = 175 #population mean
    sigma = 15 #population standard deviation
    LowLim = mu - 5 * sigma #lower limit for integration of GNPDF
    #step 2.
    pMin=Simpson(GNPDF,(mu,sigma), mu-20*sigma, LowLim,nPoints=100) #a lower limit for p values
    Probs=[] #an empty list for storing probability values
    X=[] #an empty list for storing x values
    p=0 #the point probability for use in lambda function
    #step 3.
    args = (mu, sigma)
    fn = lambda x: p-Simpson(GNPDF, (mu,sigma), LowLim, x, nPoints=100) #callback for Secant
    #step 4.
    for i in range(1000): #I want 1000 values
        p,seeds =GetRandInt(seeds) #use random number generator to get p and new seeds
        p, oClamped = Clamp(p, pMin, 1.0) #$JES Missing Code$ #clamp p between pMin and 1.0
        if oClamped:
            pass #this was just for debugging
        Probs.append(p) #append list of probabilities
        x=Secant(fn,mu,mu+sigma,maxiter=100, xtol=1e-6) #find x corresponding to p
        X.append(x) #append x to X
    #step 5.
    print('P= \r\n',Probs)
    print('X= \r\n',X)
    M = (sum(X)/len(X)) #calculate sample mean
    ss= Variance(M, X)/(len(X)-1) #estimate population variance
    print('\r\nPopulation mean estimate = {:0.2f}'.format(M))
    print('Population variance estimate = {:0.2f}'.format(ss))
    print('Population standard deviation estimate = {:0.2f}'.format(ss**0.5))
main()