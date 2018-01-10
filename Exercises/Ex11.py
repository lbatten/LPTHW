# Exercise 11: Asking Questions #
###############################

print "How old are you?"
age = raw_input()
print "How tall are you?",
height = int(raw_input())
print "How much do you weigh?",
weight = int(raw_input())

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

height2 = height/100.00
print height2

BMI = weight/(height2*height2)
print "That means your BMI is:", BMI

# OUTPUT #
##########
# $ python Ex11.py
# How old are you? 33
# How tall are you? 165
# How much do you weigh? 78
# So, you're '33' old, '165' tall and '78' heavy.

# BMI #
#######
# 1.65
# That means your BMI is: 27.9155188246

# Notes #
#########
# Aha moment!!
# If height is entered in feet and inches e.g. 5'2" then
# it is returned as '5\'5"' using the escape backslash to
# make sure python knows it is not the end of the string.
