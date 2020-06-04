
#Autor: Mariana Soeiro
#About: Exercicio 6 - Lista 4 (Python)

# - 6. Convert temperatures from Celsius to Fahrenheit [x]

def toCelsius() :
    print("my converter from Celsius to Fahrenheit ")
    # 1.8c + 32 = F

    c = float(input("Choose a temperatura in Celsius degrees to convert in Fahrenheit degrees "))
    f = c * 1.8 + 32
    print("The temperature is {0} degrees Celsius is {1} degrees Fahrenheit".format(c,f))
toCelsius()

def toFahrenheit() :
    print("my converter from Fahrenheit to Celsius")
    # (f - 32) * 1.8
    f = float(input("Choose a temperatura in Fahrenheit degrees to convert in Celsius degrees "))
    c = (f - 32)/1.8
    print("The temperature is {0} degrees Fahrenheit is {1} degrees Celsius".format(f,c))

toFahrenheit()

