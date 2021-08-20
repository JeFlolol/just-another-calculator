# draft inputArg section 
#we take input from prompt
#put it in input()
#take the output of input() and put it in int()
#take output of int() and put it in our add()

# draft InputOp section
# we put a arg in input()
# check if "add" is  returned
# if "add" is returned 
# execute InputArg section
# else display error msg

def add(arg1,arg2):
    sumResult = arg1 + arg2
    return sumResult
    
#print(add(5,7))

# inputOp section 
InputOp = input("Enter operation:  ")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
if(InputOp == "add"):
   
    # inputArg section 
    InputArg = input("enter argument 1: ")
    convInputArg1 = int(InputArg)  #impo: create error handler for string input
    InputArg = input("enter argument 2: ")
    convInputArg2 = int(InputArg)  #impo: create error handler for string input
    # print(InputArg)
    # print(type(InputArg))
    # print("-----")
    # print(convInputArg)
    # print(type(convInputArg))

    print(add(convInputArg1,convInputArg2)) 
   
else: 
    print("You did not spcefy corrcet oparation")
    print("Available oparations are: \n")
    print("...add")


#inputArg section 
# InputArg = input("enter argument 1: ")
# convInputArg1 = int(InputArg)  #impo: create error handler for string input
# InputArg = input("enter argument 2: ")
# convInputArg2 = int(InputArg)  #impo: create error handler for string input
# print(InputArg)
# print(type(InputArg))
# print("-----")
# print(convInputArg)
# print(type(convInputArg))

# print(add(convInputArg1,convInputArg2)) 
