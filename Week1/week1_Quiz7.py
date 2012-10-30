#sides, n, and the length of each side, s


import math

PI = math.pi

def areaPolygon (n,s):
    area = (0.25 * n * (s**2) ) / math.tan(PI/n)
    return area

#5 sides, each of length 7 inches, has area 84.30339262885938 square inches.

print "5 sides, length 7 , has area 84.30339262885938 : ", areaPolygon(5,7)

print "7 sides, length 3  : ", areaPolygon(7,3)