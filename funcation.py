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