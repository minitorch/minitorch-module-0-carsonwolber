"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
def mul(a: float, b:float):
  return a * b 
# - id
def id(a): # type: ignore
  return a
# - add
def add(a: float, b:float):
  return a + b
# - neg
def neg(a: float):
  return -1 * a
# - lt
def lt(a: float, b:float):
  return a < b
# - eq
def eq(a: float, b:float):
  return a == b
# - max
def max(a: float, b:float):
  if a > b :
    return a
  return b 
# - is_close
def is_close(a: float, b: float):
  return abs(a - b) < .01
# - sigmoid
def sigmoid(x: float):
  if x >= 0:
    return 1.0 / (1.0 + math.e ** -x)
  return math.e**x / (1.0 + math.e**x)
# - relu
def relu(x: float):
  return max(x, 0)
# - log
def log(x: float):
  return math.log(x, math.e)
# - exp
def exp(x:float):
  return math.e ** x
# - log_back
def log_back(a: float, b: float):
  return 1/a * b
# - inv
def inv(a: float):
  return 1/a
# - inv_back
def inv_back(a: float, b:float):
  (-1/a**2) * b 
# - relu_back
def relu_back(x: float, y:float):
  if max(x,0) == x:
    return y
  return 0
  
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
