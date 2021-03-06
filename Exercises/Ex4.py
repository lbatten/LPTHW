# Exercise 4: Variables And Names #
###################################

# Set variable cars to 100
# there are 100 cars
cars = 100

# Set variable space_in_a_car to 4
# there are 4 spaces in a car
space_in_a_car = 4.0

# Set variable drivers to 30
# there are 30 drivers
drivers = 30

# Set variable passengers to 90
# there are 90 oassengers
passengers = 90

# Set variable cars_not_driven to calculate the number of cars not driven
# number of cars minus the number of drivers
cars_not_driven = cars - drivers

# Set variable cars_driven to calculate the number of cars driven
# equals the number of drivers
cars_driven = drivers

# Set variable carpool_capacity to calculate the number of spaces available in a car
# number of cars multiplied by number of spaces in a car
carpool_capacity = cars_driven * space_in_a_car

# Set variable average_passengers_per_car to calculate the average number of passengers in a car
# number of passengers divided by number of cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "passengers in each car."

# STUDY DRILLS #
################
# Set variable average_people_per_car to calculate the average number of people in a car including the driver
# carpool capacity divided by number of cars driven
average_people_per_car = carpool_capacity / cars_driven
print "Which is", average_people_per_car, "in each car including the driver."

# I carried you the test above to check that the problem wasn't with the logic, but with the syntax
# The error in the teacher's line 8 (which corresponds to my line 31) is that
# he set the variable as "carpool_cap" and then used "car_pool_cap" to call it
# this meant that the system did not recognise the name of the variable called

# What happens if we use 4 instead of 4.0 in line 7?
# This does not seem to make any difference to the outcome, except for the "floating point"

# Using python as a calculator #
# $ cars = 100
# $ drivers = 30
# $ cars_not_driven = cars - drivers
# $ print cars_not_driven
# $ 70
