# Exercise 15: Reading files #
#################################################

# ask python to use an argv variable
from sys import argv

# Tells the program to run the sript file and use the filename as the argv
script, filename = argv

# opens a txt file with name filename
txt = open(filename)

# prints a sentence to introduce your file
print "Here's your file %r:" % filename
# reads the texts file and prints output
print txt.read()

# asks for user to input the name of the txt file again
print "Type the filename again:"
# creates a variable to hold the filename
file_again = raw_input("> ")

# opens a txt file with name filename
txt_again = open(file_again)

# reads the texts file and prints output
print txt_again.read()

# OUTPUT #
##########
# $ python Ex15.py ex15_sample.txt
# Here's your file 'ex15_sample.txt':
# This is studd I styped into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

# Type the filename again:
# > ex15_sample.txt
# This is studd I styped into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

# * IN THE PYTHON SHELL *
# >>> filename = "ex15_sample.txt"
# >>> txt = open(filename)
# >>> print txt.read()
# This is studd I styped into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

#################################################
