import random
# import random to find random integers

# Create the random integer program for seeds, according to the Wichmann-Hill algorithm.
def GetRandInt(s1, s2, s3):
    """
    This program uses the Wichmann-Hill algorithm to find random integers for seeds.
    :param s1: seed value 1 to be stored in the tuple
    :param s2: seed value 2 to be stored in the tuple
    :param s3: seed value 3 to be stored in the tuple
    :return: r, s1, s2, s3
    """
    # Wichmann-Hill algorithm
    s1 = (171 * s1) % 30269
    s2 = (172 * s2) % 30307
    s3 = (170 * s3) % 30323
    r = ((s1 / 30269.0) + (s2 / 30307.0) + (s3 / 30232.0)) % 1
    return [r, s1, s2, s3]

def findDuplicates(A):
    """
    I'm trying to find if there are duplicate numbers in my matrix A.
    I know if I did this on paper, i would point to element A[0][0] and then scan through all the other elements
    to see if A[0][0] is used more than once.  Then I would move to A[0][1] and scan again.  Keep repeating until I have
    verified all elements of A. Count all but the element I'm pointing at, so duplicate isn't mistaken.
    :param A: Matrix A, a 10x10 matrix
    :return: Validation or lack thereof for duplicated values in A
    """
    # Verify there are no duplicated numbers in matrix A
    # Create a list 'nDup' to store matrix elements
    nDup = []

    # for every element in A
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            # If the value is in 'nDup', the element is being repeated, return "Invalid."
            if A[i][j] in nDup:
                return "Invalid response. {.d} are duplicated numbers.".format(nDup)
            # If the value is not in 'nDup,' it is the first use & is appended to 'nDup.'
            else:
                nDup.append(A[i][j])

    # Return verified, if there aren't any duplicated values in A.
    return "Valid response. No duplicated numbers."

def main():
    """
    This program is finishing my matrix A by calling the previous functions and printing the final matrix, seeds,
    and validation of the matrix A.
    :return: Solution for matrix A, seeds, and validation/invalidation of duplicated numbers.
    """
    # Create original list for A where values are defaulted between 0 and 1
    mylist = []
    for i in range(4, 1000):
        x = random.random()
        mylist.append(x)
    # print(mylist)

    # Denote given seed values and assign the tuple accordingly
    seeds = [1234, 19857, 25000]
    row = 10
    col = 10
    s1, s2, s3 = seeds

    # Append the Matrix A according to parameters given, removing any duplicated values into the 10x10 matrix
    A = []
    dictionary = {}
    for i in range(0, 10):
        row =[]
        count = 0
        # While loop to create the 10x10 matrix, multiplying the smaller values by 100 to be within range(0,99)
        while count < 10:
            r, s1, s2, s3 = GetRandInt(s1, s2, s3)
            r = int(r * 100)
            # Removing any duplicated integers, only adding them once to matrix A
            if r not in dictionary:
                row.append(r)
                dictionary[r] = True
                count = count + 1
        A.append(row)

    # Print the new matrix A and given seed values
    print("A = ", A)

    print("Seed values = ", seeds)

    print(findDuplicates(A))

main()