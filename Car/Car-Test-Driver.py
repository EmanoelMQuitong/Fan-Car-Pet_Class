from Car import Car
import pyfiglet
from colored import fg

#pyfiglet format :
# color = fg('blue')
#text_print = (f"Text")
#print(color + pyfiglet.figlet_format(text_print , font= "digital")) 
color = fg('blue')
#Colors
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'
BORDER = 100*'='
print(YELLOW+BOLD+BORDER+END)
print(YELLOW+BOLD+BORDER+END)

print(GREEN+BOLD+"Inputs: "+END)

year = input("Insert year model: ")
make = input("Insert the body make: ")

print('\n')

print(YELLOW+BOLD+BORDER+END)
print(YELLOW+BOLD+BORDER+END)

car1 = Car(year, make)

print(BLUE+BOLD+"Status: "+END)
car1.show()

print('\n')

print(YELLOW+BOLD+BORDER+END)
print(YELLOW+BOLD+BORDER+END)
print(GREEN+BOLD+"Accelerate: "+END)

for x in range(5):
    car1.accelerate()

print('\n')

print(BOLD+BORDER+END)

print(BLUE+BOLD+"Status: "+END)
car1.show()

print('\n')

print(BOLD+BORDER+END)
print(BOLD+BORDER+END)

print(GREEN+BOLD+"Brake: "+END)

for x in range(5):
    car1.brake()

print('\n')

print(BOLD+BORDER+END)

print(BLUE+BOLD+"Status: "+END)
car1.show()

print('\n')

print(BOLD+BORDER+END)
print(BOLD+BORDER+END)