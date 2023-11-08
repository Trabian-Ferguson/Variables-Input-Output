# Purpose: This program calculates the amount and cost of purchasing flooring.



#intitalizing varibales and receiving input

l = input("Room Length: ")

w = input("Room Width: ")

cost = input("Cost per Sq. Foot ")

# casting from string to a "float"

l = float(l)

w = float(w)

cost = float(cost)

#calculations

sqft = (l*w) #this is for output 1

floor = (sqft*cost) #this is for output 2

tax = (floor*0.07) # this is for output 3

total = (floor+tax)


# output

print ("Square feet:",sqft)

print ("Flooring:",floor)

print ("Tax:",tax )

print ("Total:",total)         
         


        
