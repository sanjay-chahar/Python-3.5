import locale
locale.setlocale(locale.LC_ALL, '')

xx = 0


basket = int(input('what is the total amount in your basket? '))
if basket >= 50 :
    print('you are elligable for free shipping!')
    xx = locale.currency(basket)
    print('your total amount to pay is ' + xx)
#    print(locale.currency(basket))
else:
    print('that will be an extra 10 pounds for shipping')
    totalamount = basket + 10
    xx = locale.currency(totalamount)

    print('your total amount to pay is ' + xx)