
from audioop import reverse
from cmath import sqrt


def sort_great_least (array):
    return array.sort(reverse=True)

def sort_least_great (array):
    return array.sort()

def distance_calc (x1, y1, x2, y2):
    xFin = (x1*x1) + (x2*x2)
    yFin = (y1*y1) + (y2*y2)
    return sqrt(xFin + yFin)
    