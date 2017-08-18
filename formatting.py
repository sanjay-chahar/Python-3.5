#Old way of formatting
name = 'Sanjay'
height = 40
weight = 70

output = "So, you're %r, %r year old, and %r heavy." % (name, height, weight)
print(output)


#New way of formatting
#similar to the old %-formatting, with the addition of the {} and with : used instead of %. For example, '%03.2f' can be translated to '{:03.2f}'.

points = 19
total = 22
print('Correct answers: {:2%}'.format(points/total))

#This will print "Correct answers: 86.363636%"

var = 'python 3'
print("This is {:}" .format(var))

#This wil print "python 3"



