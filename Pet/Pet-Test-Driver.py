from Pet import Pet
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

print(BOLD+BORDER+END)
print(BOLD+BORDER+END)

pet1 = Pet('Peter Griffin', 'Beluga Whale', 89)

print(PURPLE+BOLD+"Sample Inputs"+END)
pet1.show()

print(BOLD+BORDER+END)
print(BOLD+BORDER+END)

print('\n')

print(DARKCYAN+BOLD+BORDER+END)
print(DARKCYAN+BOLD+BORDER+END)

print(BLUE+BOLD+"Enter your pet's data: "+END)

name = input("Enter the name of your pet: ")
animal_type = input("Enter the animal type of your pet: ")
age = input("Enter the age of your pet in month: ")

pet1.set_name(name)
pet1.set_animal_type(animal_type)
pet1.set_age(age)


print(DARKCYAN+BOLD+BORDER+END)
print(DARKCYAN+BOLD+BORDER+END)

print('\n')

print(DARKCYAN+BOLD+BORDER+END)
print(DARKCYAN+BOLD+BORDER+END)

print(BLUE+BOLD+"Pet Information: "+END)
pet1.show()

history = open('History.txt', 'a')
history.write("Animal name: "),history.write(pet1.get_name()), history.write('\n')
history.write("Animal Type: "),history.write(pet1.get_animal_type()), history.write('\n')  
history.write("Age: "),history.write(str(pet1.get_age())), history.write('\n'), history.write('\n') 
history.close()

print('\n')

print(GREEN+BOLD+"Thank you for your cooperation."+END)
print(GREEN+BOLD+"Your information has been successfuly saved."+END)
print(DARKCYAN+BOLD+BORDER+END)
print(DARKCYAN+BOLD+BORDER+END)