# DistanceBetweenPointsCalculator.py
# Your job is to write a function in DistanceBetweenPointsCalculator.py (call
# it **calculateDistanceBetween()** that calculates the distance between two points
# in 2D space (x1, y1) and (x2, y2)
# based on The Distance Formula
# mathwarehouse.com (http://www.mathwarehouse.com/algebra/distance_formula/index.php)

# Define Function below
# be sure to return an integer


import math

def calculateDistanceBetween(x1,y1,x2,y2):
    Distance=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
    Distance=round(Distance,2)
    return Distance



if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
    
