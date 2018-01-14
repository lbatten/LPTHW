# Exercise 13: Parameters, Unpacking, Variables #
#################################################

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# OUTPUT #
##########
# The script is called: ex13.py
# Your first variable is: first
# Your second variable is: second
# Your third variable is: third

#################################################

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", raw_input()

# Your first variable is: first
# Your second variable is: second
# Your third variable is: (...)
# third
