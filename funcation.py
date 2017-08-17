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
    filename = input('please enter full file name and path :- ')
    filename = open(filename, mode='w')
    filename = filename.write(messages)
    readfile(filename)
    return

def readfile(filename):
    open(filename, mode='r')
    read(filename)
    filename()
    return
main()