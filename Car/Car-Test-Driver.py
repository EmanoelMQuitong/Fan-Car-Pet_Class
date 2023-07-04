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



year = input("Insert year model: ")
make = input("Insert the body make: ")

car1 = Car(year, make)

for x in range(5):
    car1.accelerate()

car1.show()