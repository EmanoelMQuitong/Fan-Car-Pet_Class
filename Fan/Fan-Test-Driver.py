from Fan import Fan
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
print(GREEN+BOLD+BORDER+END)
print(GREEN+BOLD+BORDER+END)

#default:
f1 = Fan()

print('\n')
print(PURPLE+BOLD+"Fan Default: "+END)
print('\n')

f1.show()
print('\n')

print(GREEN+BOLD+BORDER+END)
print(GREEN+BOLD+BORDER+END)

print('\n')
print(BOLD+BORDER+END)
print(BOLD+BORDER+END)

#object 1
print('\n')

print(BLUE+BOLD+"Fan 1:"+END)

speed = input("How fast do you want your fan?('SLOW','MEDIUM', or 'FAST'): ")
radius = input("How wide is your fan blades?('5.0' to '10.0'): ")
color = input("Which color do you like?: ")
power = input("Do you want to turn it on?: ")

f2 = Fan(speed, radius, color, power)
print('\n')
print('\n')

print(RED+BOLD+"Fan 1:"+END)

print('\n')

print("Fan speed: ",f2._Fan__speed)
print("Fan blade Radius: ", f2._Fan__radius)
print("Fan Color: ", f2._Fan__color)
print("Power on?: ", f2._Fan__on)

print('\n')
print(BOLD+BORDER+END)
print(BOLD+BORDER+END)

print('\n')

print(PURPLE+BOLD+BORDER+END)
print(PURPLE+BOLD+BORDER+END)

#object 1
print('\n')

print(YELLOW+BOLD+"Fan 2:"+END)

speed = input("How fast do you want your fan?('SLOW','MEDIUM', or 'FAST'): ")
radius = input("How wide is your fan blades?('5.0' to '10.0'): ")
color = input("Which color do you like?: ")
power = input("Do you want to turn it on?: ")

f3 = Fan(speed, radius, color, power)

print('\n')
print('\n')

print(YELLOW+BOLD+"Fan 2:"+END)

print('\n')

print("Fan speed: ",f3._Fan__speed)
print("Fan blade Radius: ", f3._Fan__radius)
print("Fan Color: ", f3._Fan__color)
print("Power on?: ", f3._Fan__on)

print('\n')
print('\n')

print(PURPLE+BOLD+BORDER+END)
print(PURPLE+BOLD+BORDER+END)