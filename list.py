# guest = []
# name = ''
#
# while name != 'Done' :
#     name = input('please enter guest name ,when finished enter Done :').capitalize()
#     guest.append(name)
#
# guest.remove('Done')
# list.sort(guest)
# print(guest)

guest = []
name = ''

while name != 'Done':
    name = input('please enter guest name ,when finished enter Done :').capitalize()
    guest.append(name)

guest.remove('Done')
list.sort(guest)
print(guest)