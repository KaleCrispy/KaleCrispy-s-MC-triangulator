import math
print("This is my Mc triangulation calculator. please ask me if you don't understand how to do it")

AngleA = (float(input("what is angle a? include decimals: ")))
print("move 10 blocks.")
AngleB_exterior = (float(input("What is angle B? include decimals: ")))

B_x = int(input("what is your X coordinate at point B where you measured your last angle?: "))
B_y = int(input("What is your Z coordinate at point B where you measured your last angle?: "))
# required to apply offset
if AngleB_exterior < 0:
    AngleB = -180 - AngleB_exterior
elif AngleB_exterior >= 0:
    AngleB = 180 - AngleB_exterior
# solves for supplementary angle
AngleC = 180-abs(AngleA+AngleB)

RadianAngleA = math.radians(abs(AngleA))
RadianAngleB = math.radians(abs(AngleB))
RadianAngleC = math.radians(AngleC)
# converts to radians and absolute value for offset calculation
k = 10/math.sin(RadianAngleC)

SideA = math.sin(RadianAngleA)*k
SideY = math.sin(RadianAngleB)*SideA
SideX = math.cos(RadianAngleB)*SideA
# applies law of sines to solve for the offset
if 90.0 > AngleB >= 0.0:
    Xcoord = B_x + SideX
    Ycoord = B_y + SideY
    Ycoord = -Ycoord
    print("coordinates:")
    print(Xcoord, Ycoord)
# ++ quadrant check
elif 180.0 > AngleB >= 90.0:
    Xcoord = B_x + SideX
    Ycoord = B_y - SideY
    Ycoord = -Ycoord
    print("coordinates:")
    print(Xcoord, Ycoord)
# +- quadrant check
elif -180.0 <= AngleB < -90.0:
    Xcoord = B_x - SideX
    Ycoord = B_y - SideY
    Ycoord = -Ycoord
    print("coordinates:")
    print(Xcoord, Ycoord)
# -- quadrant check
elif -90.0 <= AngleB < 0.0:
    Xcoord = B_x - SideX
    Ycoord = B_y + SideY
    Ycoord = -Ycoord
    print("coordinates:")
    print(Xcoord, Ycoord)
# -+ quadrant check
