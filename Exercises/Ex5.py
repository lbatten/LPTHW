# Exercise 5: More Variables And Printing #
###########################################

my_name = "Ligaya Batten"
my_age = 33
my_height = 165 # cm
my_weight = 78 # kilos
my_eyes = "Brown"
my_teeth = "White"
my_hair = "Black"

print "Let's talk about %s." % my_name
print "She's %d centimetres tall." % my_height
print "She weighs %d kilos." % my_weight
print "That's quite heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# OUTPUT
########
# $ python Ex5.py
# Let's talk about Ligaya Batten.
# She's 165 centimetres tall.
# She weighs 78 kilos.
# That's quite heavy.
# She's got Brown eyes and Black hair.
# Her teeth are usually White depending on the coffee.
# If I add 33, 165, and 78 I get 276.

# STUDY DRILLS
##############

name = "Ligaya Batten"
age = 33
height = 165 # cm
weight = 78 # kilos
eyes = "brown"
teeth = "white"
hair = "black"

print "Let's talk about %s." % name
print "She's %e centimetres tall." % height
print "She weighs %f kilos." % weight
print "That's quite heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# %d - decimal integer
# %s - string
# %f - float (default 6dp)
# %e - (float - exponential notation *standard form)
# %r - any string (raw)
