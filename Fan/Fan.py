class fan:
    def __init__(self, speed = 1, radius = 5, color = 'blue', on = False):
        self.__speed = int(speed)
        self.__radius = float(radius)
        self.__on = bool(on)
        self.__color = str(color)

    def speed(self, speed):
        speed = speed.upper()
        if speed == 'SLOW' or speed == 'MEDIUM' or speed == 'FAST':
            if speed == 'SLOW':
                return speed == 1
            elif speed == 'MEDIUM':
                return speed == 2
            elif speed == 'FAST':
                return speed == 3

        else:
            print("Please choose from 'SLOW', 'MEDIUM', and 'FAST' only.")
    
    def show(self):
        print("Speed: ", self.__speed)
        print("Radius: ", self.__radius)
        print("Is it on?: ", self.__on)
        print("Color: ", self.__color)
    
f = fan()
f.show()
