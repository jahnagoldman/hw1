# solution_8.py
# A program to convert Fahrenheit temperatures into Celsius
def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * (5/9)
    print("The temperature is", celsius, "degrees Celsius.")

main()
