import turtle
user = int(input('how many side you need your object '))
for step in range(user):
    turtle.forward(200)
    turtle.left(360 / user)
    for morestep in range(user):
        turtle.forward(100)
        turtle.left(360 / user)

for nums in range(1,10,2):
    print(nums)


for clours in ['red', 'blue','green','yellow']:
    turtle.color(clours)
    turtle.forward(200)
    turtle.left(360 /user)




