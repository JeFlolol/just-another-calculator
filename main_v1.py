#!/usr/bin/env python3

# Draft for InputArg section
# we take input from prompt
# put it in input()
# take the output of input() and put it in int()
# take output of int() and put it in our add()

# Draft for InputOp section
# we put a arg in input()
# check if "add" is returned
# if "add" is returned
# execute InputArg section
# else display error msg

def add(arg1,arg2):
    sumResult = arg1 + arg2
    return sumResult

# print(add(5,7))

### InputOp section
InputOp = input("Enter operation: ")
# # dummy debug
# x = 10
# if (x == 10):
if (InputOp == "add"):
    ### InputArg section
    InputArg = input("Enter argument 1: ")
    convInArg1 = int(InputArg)       # IMPO: create error handler for string input
    InputArg = input("Enter argument 2: ")
    convInArg2 = int(InputArg)       # IMPO: create error handler for string input
    # print(InputArg)
    # print(type(InputArg))
    # print("--------")
    # print(convInArg)
    # print(type(convInArg))
    print(add(convInArg1,convInArg2))
else:
    print("You did not specity correct operation\n")
    print("Available operations are: \n")
    print("--- add")

# ### InputArg section
# InputArg = input("Enter argument 1: ")
# convInArg1 = int(InputArg)       # IMPO: create error handler for string input
# InputArg = input("Enter argument 2: ")
# convInArg2 = int(InputArg)       # IMPO: create error handler for string input
# # print(InputArg)
# # print(type(InputArg))
# # print("--------")
# # print(convInArg)
# # print(type(convInArg))

# print(add(convInArg1,convInArg2))
