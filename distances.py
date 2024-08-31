#@author: GaloisField
#@desc: Compute normes and distances

import numpy as np
from datetime import datetime


############################################
# Euclidean distance between two vectors
# X and Y are tuples of the same length
# Returns the distance between X and Y
############################################


################################
# Operations on vectors
################################


# Opposite of a vector
def opp(X):
    n = len(X)
    Y = ()
    for i in range(n):
        Y += (-X[i],)
    return Y


# Add two vectors
def add(X, Y):
    if len(X) != len(Y):
        return None
    n = len(X)
    Z = ()
    for i in range(n):
        Z += (X[i] + Y[i],)
    return Z

# Substract two vectors
def sub(X, Y):
    if len(X) != len(Y):
        return None
    n = len(X)
    o_Y = opp(Y)
    Z = add(X, o_Y)
    return Z


# Multiply two vectors
def mul(X, Y):
    if len(X) != len(Y):
        return None
    n = len(X)
    Z = ()
    for i in range(n):
        Z += (X[i] * Y[i],)
    return Z

# Power of a vector
def power(X, p):
    n = len(X)
    Y = ()
    for i in range(n):
        Y += (X[i]**p,)
    return Y

################################
# Normes and distances
################################

# Distance over Norm2 of a vector
def dist(X,Y):
    if len(X) != len(Y):
        return None
    
    diff = sub(X,Y)
#    print(f"X-Y = ", diff)

    square_diff = power(diff, 2)
#    print("(X-Y)^2 = ", square_diff)

    sum_square = sum(square_diff)
#    print("Sigma (xi - yi)^2 = ", sum_square)

    d = np.sqrt(sum_square)
#    print("Sqrt(Sigma (xi-yi)^2) = ", d)

    return d

def norm2(X):
    N = dist(X, (0,) * len(X))
    return N

# Distance over Norm3 of a vector
def dist3(X,Y):
    if len(X) != len(Y):
        return None
    
    o_Y = opp(Y)
#    print("-Y = ", o_Y)
    
    diff = add(X,o_Y)
#    print(f"X-Y = ", diff)
    cube_diff = power(diff,3)
#    print("(X-Y)^3 = ", cube_diff)
    
    sum_cube = sum(cube_diff)
#    print("Sigma (xi - yi)^3 = ", sum_cube)
        
    d = np.cbrt(sum_cube)
#    print("Cbrt(Sigma (xi-yi)^3) = ", d)
    return d

def norm3(X):
    N = dist3(X, (0,) * len(X))
    return N


# Test

#time_X = datetime(2020, 1, 1, 12, 0, 0)
#time_Y = datetime(2017, 1, 31, 12, 0, 10)
#time_dist = time_X - time_Y
#
#
#X = (50, 25, 31, 47)
#Y = (80, 60, 70, 62)
#
#print("\n\n Test \n\n")
#
#print("X = ", X)
#print("Time X = ", time_X, "\n")
#
#print("Y = ", Y)
#print("Time Y = ", time_Y)
#
#
#print("\n\n Computation \n\n")
#d = dist(X,Y)
#
#print("\n\n Results\n\n")
#
#print("Candles distance is ", d, "\n")
#print("Time distance is ", time_dist)
#
#
#print("\n\n")
