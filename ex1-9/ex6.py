#Assignment of a string with a number formatter and said number
x = "There are %d types of people." % 10
#String assignments
binary = "binary"
do_not = "don't"
#Assignment of a string with string formatters and strings 
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e