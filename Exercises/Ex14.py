# Exercise 14: Prompting and Passing #
#################################################

from sys import argv

script, user_name = argv
prompt = 'Enter your answer here: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)


# OUTPUT #
##########
# (py27) Ligayas-Macbook:Exercises Ligaya$ python Ex14.py Ligaya
# Hi Ligaya, I'm the Ex14.py script.
# I'd like to ask you a few questions.
# Do you like me Ligaya?
# Enter your answer here: yes
# Where do you live Ligaya?
# Enter your answer here: London
# What kind of computer do you have?
# Enter your answer here: Apple Mac

# Alright, so you said 'yes' about liking me.
# You live in 'London'. Not sure where that is.
# And you have a 'Apple Mac' computer. Nice.

#################################################
