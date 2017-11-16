
"""
This module provides functions to perform standard vector operations.  Vectors
are represented as lists of numbers (floats or ints).  Functions that take two 
vector arguments may give arbitrary output if the vectors are not compatible,
i.e. of the same dimension.  
"""
import math
import random

def add(u, v):
    """Return the vector sum u+v."""
    answer = [u[i]+v[i] for i in range(len(u))]
    return answer

def negate(u):
    """Return the negative -u of the vector u."""
    answer = [-a for a in u]
    return answer

def sub(u, v):
    """Return the vector difference u-v."""
    v = [-b for b in v]
    answer = [u[i]+v[i] for i in range(len(u))]
    return answer

def scalarMult(c, u):
    """Return the scalar prdocut cu of the number c by the vector u."""
    answer = [a * c for a in u]
    return answer

def zip(u, v):
    """Return the component-wise product of with v."""
    answer = [u[i]*v[i] for i in range(len(u))]
    return answer

def dot(u, v):
    """Return the dot product of u with v."""
    answer = sum(zip(u,v))
    return answer

def length(u):
    """Return the (geometric) length of the vector u."""
    squared = [i**2 for i in u]
    total = sum(squared)
    answer = math.sqrt(total)
    return answer

def unit(v):
    """Return a unit (geometric length l) vector in the direction of v."""
    squared = [i**2 for i in v]
    total = sum(squared)
    sqrt = math.sqrt(total)
    answer = [i/sqrt for i in v]
    return answer

def angle(u, v):
    """
    Return the angle (in degrees) between vectors u and v.
    """
    return math.degrees(math.acos(dot(unit(u),unit(v))))

def randVector(n, a, b):
    """ Return the vector of dimension n whose components are random floats in the range [a, b)."""
    answer = []
    for i in range(n):
        component = random.uniform(a,b)
        answer.append(component)
    return answer
