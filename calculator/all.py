from operations.addition import addition
from operations.substraction import substraction
from operations.multiplication import multiplication
from operations.division import division
from operations.exponentiation import exponentiation
from operations.modulus import modulus

moni = input("""Greetings, please enter the mathematical operation you wish to execute, considering that:

1 = addition
2 = subtraction
3 = multiplication
4 = division
5 = exponentiation
6 = modulus
Plase choose the number: 
""")

a = float(input("Thank you very much. Please proceed to enter the first number: "))
b = float(input("Enter the second number: "))

if moni == '1':
    print(f"Result of addition: {addition(a, b)}")
elif moni == '2':
    print(f"Result of subtraction: {substraction(a, b)}")
elif moni == '3':
    print(f"Result of multiplication: {multiplication(a, b)}")
elif moni == '4':
    print(f"Result of division: {division(a, b)}")
elif moni == '5':
    print(f"Result of exponentiation: {exponentiation(a, b)}")
elif moni == '6':
    print(f"Result of modulus: {modulus(a, b)}")
print("Thank you for using this calculator. Have a great day!")
