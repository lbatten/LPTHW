# Exercise 8: Printing, Printing #
##################################

# create variable called formatter to combine 4 strings
formatter = "%r %r %r %r"

# insert integers into the %rs in formatter
print formatter % (1, 2, 3, 4)
# insert number words into the %rs in formatter
print formatter % ("one", "two","three", "four")
# insert Booleans into the %rs in formatter
print formatter % (True, False, False, True)
# insert the var formatter into the %rs in formatter
print formatter % (formatter, formatter, formatter, formatter)
# insert strings into the %rs in formatter
print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
)


# OUTPUT #
##########
# $ python Ex8.py
# 1 2 3 4
# 'one' 'two' 'three' 'four'
# True False False True
# '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
