# 5th april, 2023.
import random
from math import*

num1 = random.randint(0,100)
num2 = random.randint(0,100)
base = random.randint(0,100)
powmethod = random.randint(0,8)
factorial_no = random.randint(0, 10)
gcd_no = random.randint(0, 10)
method = random.choice(["+","-","*","/","^","!","gcdm"])
insult =["bozo.", "I expected more from you.", "Appalling.", "just quit math, man.", "beyond shameful." , "just use a calculator.", "bucko"]
 
print("Solve the following mathematical problem.")
# Basic operations
def calc(num1 , method , num2): 
    wrong = 0
    while method  == "+":
        if wrong == 3:
            print("You ran out of tries.")
            quit()
        result = num1 + num2
        print(str(num1)+  "+" +str(num2) + "= " )
        ans = input("Enter your answer here : ")
        if result == int(ans):
            print("Correct answer.")
            quit()
        elif result != int(ans):
            print("incorrect answer, " + random.choice(insult))
            wrong +=1
          
    wrong = 0
    while method  == "-":
        if wrong == 3:
            print("You ran out of tries.")
            quit()
        result = num1 - num2
        print(str(num1)+  " - " +str(num2) + "= " )
        ans = input("Enter your answer here : ")
        if result == int(ans):
            print("Correct answer.")
            quit()
        elif result != int(ans):
            print("incorrect answer, " + random.choice(insult))
            wrong +=1
          
    wrong = 0
    while method  == "*":
        if wrong == 3:
            print("You ran out of tries.")
            quit()
        result = num1 * num2
        print(str(num1)+  " x " +str(num2) + "= " )
        ans = input("Enter your answer here : ")
        if result == int(ans):
            print("Correct answer.")
            quit()
        elif result != int(ans):
            print("incorrect answer, " + random.choice(insult))
            wrong +=1
                
    wrong = 0
    while method  == "/":
        if wrong == 3:
            print("You ran out of tries.")
            quit()
        result = num1 / num2
        print(str(num1)+  "/" +str(num2) + "= " )
        ans = input("Enter your answer here : ")
        if result == float(ans):
            print("Correct answer.")
            quit()
        elif result != float(ans):
            print("incorrect answer, " + random.choice(insult))
            wrong +=1

#The power function
def power (base, powmethod):
    wrong = 0
    while method  == "^":
        if wrong == 3:
            print("You ran out of tries.")
            quit()
        result = pow(base, powmethod)
        print(str(base)+  " ^ " +str(powmethod) + " = " )
        ans = input("Enter your answer here : ")
        if result == int(ans):
            print("Correct answer.")
            quit()
        elif result != int(ans):
            print("incorrect answer, " + random.choice(insult))
            wrong +=1
            
# The factorial function
def funcfact(factorial_no):
    wrong = 0
    while method  == "!":
        if wrong == 3:
            print("You ran out of tries.")
            quit()
        result = factorial(factorial_no)
        print(str(factorial_no)+  "!"  + "= " )
        ans = input("Enter your answer here : ")
        if result == int(ans):
            print("Correct answer.")
            quit()
        elif result != int(ans):
            print("incorrect answer, " + random.choice(insult))
            wrong +=1

# Greatest common divisor function
def greatest_common_divisor(no1, no2): 
    wrong = 0
    print("Find the greatest common divisor.")
    while method  == "gcdm":
        if wrong == 3:
            print("You ran out of tries.")
            print("The correct answer is " + str(gcd(factorial_no, gcd_no)))
            quit()
        result = gcd(factorial_no, gcd_no)
        print(str(factorial_no) + ' , ' + str(gcd_no) + " = " )
        ans = input("Enter your answer here : ")
        if result == int(ans):
            print("Correct answer.")
            quit()
        elif result != int(ans):
            print("incorrect answer, " + random.choice(insult))
            wrong +=1


#Calling the functions
calc(num1 , method , num2)
power(base,powmethod)
funcfact(factorial_no)
greatest_common_divisor(factorial_no, gcd_no)