
#Autor: Mariana Soeiro
#About: Exercicio 6 - Lista 4 (Python)

# - 6. Convert temperatures from Celsius to Fahrenheit [x]

def menu() :
    print("\n   1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    pick = int(input("Choice the temperature: "))#Input
    return pick

def toCelsius(c) :
    print("my converter from Celsius to Fahrenheit ")
    # 1.8c + 32 = F
    return float(c * 1.8 + 32)
    #print("The temperature is {0} degrees Celsius is {1} degrees Fahrenheit".format(c,f))
toCelsius()

def toFahrenheit() :
    print("my converter from Fahrenheit to Celsius")
    # (f - 32) * 1.8
    return (f - 32)/1.8
   # print("The temperature is {0} degrees Fahrenheit is {1} degrees Celsius".format(f,c))
toFahrenheit()

def main():
    choice = menu()
    while choice != 3:
        if choice == 1:
            print("The temperature is {0} degrees Celsius is {1} degrees Fahrenheit".format(c,f))
        elif choice == 2:
            print("The temperature is {0} degrees Fahrenheit is {1} degrees Celsius".format(f,c))
        else:
            print("Invalid Entry")
    choice = menu()  
main()

