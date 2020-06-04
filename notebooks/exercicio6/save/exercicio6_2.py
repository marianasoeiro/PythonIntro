
#Autor: Mariana Soeiro
#About: Exercicio 6 - Lista 4 (Python)

# - 6. Convert temperatures from Celsius to Fahrenheit.

def menu() :
    print("\n 1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    pick = int(input("Choice the temperature: "))#Input
    return pick
    
def toCelsius(f):
    return int((f - 32)/1.8)
    
def toFahrenheit(c):
    return int(c * 1.8 + 32)
    
def main():
    choice = menu()
    while choice != 3:
        if choice == 1:
            #convert Celsius to Fahrenheit
            #c = eval(input("Enter degrees Celsius: "))
            print(str(toFahrenheit(c)))
        elif choice == 2:
            #convert Fahrenheit to Celsius
            f = eval(input("Enter degrees Fahrenheit: "))
            print(str(toCelsius(f)))
        else:
            print("Invalid Entry")
    choice = menu()  
main()
