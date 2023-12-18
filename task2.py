import math
#For this task i am required to calculate the area that the foundation of a building covers.
#User will need to enter the shape of the building and user can only enter:
    #Square, rectangular and round.
print("Step 1:")
print("Words to describe the shape of foundation:")
print("Square")
print("Rectangular")
print("Round.")

building_shape = str(input("Enter shape of building: "))

if building_shape == "Square":
    print("Valid entry.")

elif building_shape == "Rectangular":
  print("Valid entry.")

elif building_shape == "Round":
  print("Valid entry.")

else: print("Enter word as shown.")

print("Step 2:")
#Based on the users shape enter I will do calculations for the correct dimensions
#○ Area of square = length of the square to the power of two (length.
#  Area of rectangle = length x width.
# Area of circle = pi x radius squared (𝛱radiussquared.
#For this parst i decided that user will have to input the measurements after they have declared the shape of foundation so if they said square they can do the calculation underneath it and it prints it out(Basically so that everything related is together.
# So If user selected Square they will do the enter values needed and calculation will be done and displayed.)

if building_shape == "Square":
 length = float(input("Enter Length of foundation: "))
 area_of_square = length * length
 print (area_of_square)

#So if user selected Rectangular they will enter the dimensions and calculation will be done and displayed."
elif building_shape == "Rectangular":
 length = float(input("Enter length of foundation: "))
 width = float(input("Enter width of foundation: "))
 area_rectangular = length *  width
 print(f"Area that will be covered is {area_rectangular}")

#If user enters Round as the building shape, they will then insert the dimension and program will calculate and display answer.
elif building_shape == "Round":
 radi_circle = float(input("Enter the raduis of the building: "))
 area_circle = math.pi * ( radi_circle ** 2)
 print(f"The area covered by foundation is {area_circle}.")

else: ("Incorrect shape entered.")





