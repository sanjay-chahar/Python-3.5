#Basic Funcation
# def main():
#     printName()
#     return
# def printName():
#     print('Hello stranger')
#     return
# main()
#little complex funcation
# def main():
#     name = str(input('Please input your name :- '))
#     message = str(input('Please enter your messages :- '))
#     msg(name, message)
#     return
# def msg(name, message):
#       print(name +  message)
#       return
# main()
#Challeneg

def main():
    messages = input('Please add your message : - ')
    path = input('please enter full file name and path :- ')
    with open(path, 'a') as filename:
        filename.write(messages + '\n')
        filename.close()
    rfile(path)
    return

def rfile(path):
    filename = open(path, 'r')
    print(filename.read())
    filename.close()
    return

main()

# Return value to funcation
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
