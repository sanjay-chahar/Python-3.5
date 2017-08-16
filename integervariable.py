import sys
#salary = input('what is your salary? ')
#bonus = input('what is your bonus? ')
#paycheck = salary + bonus
#print(paycheck)

#challenge
loan = input('what is your loan amount? ')
interestrate = input('what is your interest rate? ')
npayments = input('what is your number of payments? ')

l = float(loan)
i = float(interestrate)
r = float(npayments)
print(l)
print(i)
print(r)
i = i/100
print("Your intereste rate is %f "  % i )

#MonthlyEMI = L[i(1+i)r]/[(1+i)r-1]
x = i*(1+i)*r

xxx = l*x

print(xxx)

y = (1+i)*r-1
print(y)
final = xxx/y
print("Your monthly EMI is %d  " % final )




print('there are three numbers.one,{0:d}.two,{1:2d}.and the third {2:4d}'.format(1,2,3))