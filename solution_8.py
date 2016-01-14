# solution_8.py
# A program to convert Fahrenheit temperatures into Celsius
def main():
    fahrenheit = eval(input("What is the temperature in degrees Fahrenheit? "))
    celsius = (fahrenheit - 32) * (5/9)
    print("Converted to Celsius, the temperature is", round(celsius), "degrees.")

main()
