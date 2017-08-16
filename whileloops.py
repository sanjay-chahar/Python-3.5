#Turtle with while loop
import turtle
length = int(input('please enter a length '))
colour = input ('please enter a colour ')
angle = int(input('please enter an angle '))
counter = 0
while counter < 4:
    turtle.color(colour)
    turtle.forward(length)
    turtle.right(angle)
    counter = counter + 1

# Answer = '0'
# while Answer != 'YES':
#     Answer = input('Please enter your answer : \n').upper()
#     print(Answer)
# print(Answer)

# num = 0
# while num < 1000:
#     print('file %d created ' % num)
#     num = num + 1



