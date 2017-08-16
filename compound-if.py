import locale
locale.setlocale(locale.LC_ALL, '')
xx = 0


basket = int(input('Please Enter your purchase amount '))
country = input('which country do you live in: ').upper()
if country == 'CANADA':
    Province = input('what province do you live in: ' ).upper()
# if country == 'CANADA' and Province == 'ALBERTA':
#     print('that will be 0.05 general sales tax')
# elif country == 'CANADA' and Province == 'ONTARIO' or Province == 'NEW BRUNSWICK' or Province == 'NOVA SCOTIA':
#     print('that will be 0.13 harmonized tax')
# elif Province != 'ONTARIO' 'NEW BRUNSWICK' 'NOVA SCOTIA' 'ALBERTA':
#     print('0.06 Provisional tax')
# else:
#     print('Thanks you for your purchase'
if country != 'CANADA':
    print('Thank you for your purchase and you don\'t need to pay tax')

elif country == 'CANADA' and Province == 'ALBERTA':
    print('that will be 0.05 general tax')
    tax = basket * 0.05
    total = basket + tax
    xx = locale.currency(total)
    print('that will be' + ' ' + xx)

elif country == 'CANADA' and (Province == 'ONTARIO' or Province == 'NEW BRUNSWICK' or Province == 'NOVA SCOTIA'):
    print('that will be 0.13 harmonized tax')
    tax2 = basket * 0.13
    total2 = basket + tax2
    xx = locale.currency(total2)
    print('that will be' +' ' + xx)
else:
    print('that will be 0.06 Provisional tax')
    tax3 = basket * 0.06
    total3 = basket + tax3
    xx = locale.currency(total3)
    print('that will be' + ' ' + xx)