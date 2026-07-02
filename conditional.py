# #if-else
# age = int(input("Enter your age:"))
# if age >=18:
#     print("you are eligeble to vote")
# else:
#     print("you are not eligible to vote")

#number = int(input("Enter a number:"))

# #if-elif
# marks = int(input("Please enter your marks:"))
# if marks>=90:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# elif marks>=50:
#     print("Grade C")
# else:
#     print("Student is not going to next class")

# #take the user input from the console and then 
# based on the input mentioned justmention for that
# amount how much discount is applixable
# #5000, 3000, 1000

# amount = float(input("Enter the amount for discount:"))
# if amount>3000 and amount<=5000:
#     print("Discount is 50%")
# elif amount>1000 and amount<=3000:
#     print("Discount is 30%")
# elif amount == 1000:
#     print("Discount is 20%")
# else:
#     print("No discount")

#Switch statemet

#  num1 = int(input("enter first number:"))
#  num2 = int(input("enter second number:"))
#  operator= input("enter operator (+,-,*,%,/):")

# match operator:
#     case "+":
#         print("Result =", num1+num2)
#     case "-":
#         print("Result =", num1-num2)
#     case "*":
#         print("Result =", num1*num2)
#     case "%":
#         print("Result =", num1%num2)
#     case "/":
#         print("Result =", num1/num2)
#     case "_":
#         print("Invalid operator")


# caluculator using if -elif
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
operator= input("enter operator (+,-,*,%,/):")

if operator == "+":
    print("Result=", num1+num2)
elif operator == "-":
    print("Result=", num1-num2)
elif operator == "*":
    print("Result=", num1*num2)
elif operator == "%":
    print("Result=", num1%num2)
elif operator == "/":
    print("Result=", num1/num2)
else:
    print("operator doesn't match")