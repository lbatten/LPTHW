# Exercise 6: Strings and Text #
################################

# create string variable x inserting 10 in types of people
x = "There are %d types of people." % 10
# create string variable binary
binary = "binary"
# create string variable do_not
do_not = "don't"
# create string variable y to insert variables binary and do_not into the sentence
y = "Those who know %s and those to %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

# create variable hilarious and set to Boolean False
hilarious = False
# create var joke_evaluation to answer question with hilarious Boolean
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# create new string var w
w = "This is the left side of... "
# create new string var e
e = "a string with a right side."

print w + e

# OUTPUT #
##########
# $ python Ex6.py
# There are 10 types of people.
# Those who know binary and those to don't.
# I said: 'There are 10 types of people.'.
# I also said: 'Those who know binary and those to don't.'.
# Isn't that joke so funny?! False
# This is the left side of... a string with a right side.
