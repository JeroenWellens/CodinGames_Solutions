import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
#a lay of the land
surface = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append((land_x,land_y))

print(f"Debug messages:{surface}", file=sys.stderr, flush=True)

# power goes from 0 to 4, with 4 counteracting the acceleration due to gravity
def determine_power(v):
    if(np.absolute(v)>39):
        return 4
    else:
        return 3

def determine_angle():
    return 0

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    #For a landing to be successful, the ship must:
    #   land on flat ground
    #   land in a vertical position (tilt angle = 0°)
    #   vertical speed must be limited ( ≤ 40m/s in absolute value)
    #   horizontal speed must be limited ( ≤ 20m/s in absolute value)

    power = determine_power(v_speed)
    angle = determine_angle()
    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    print(f"{angle} {power}")
