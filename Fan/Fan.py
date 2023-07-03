class Fan:
    def __init__(self, speed = 'SLOW', radius = 5, color = 'blue', on = False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__on = bool(on)
        self.__color = str(color.lower())

    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        speed = speed.upper()
        if speed == 'SLOW' or speed == 'MEDIUM' or speed == 'FAST':
            if speed == 'SLOW':
                self.__speed = int(1)
            elif speed == 'MEDIUM':
                self.__speed = int(2)
            elif speed == 'FAST':
                self.__speed = int(3)

        else:
            print("Please choose from 'SLOW', 'MEDIUM', and 'FAST' ONLY.")
    
    def on(self, on):
        on = on.lower()
        if on == 'yes' or on == 'no':
            if on == 'yes':
                return True
            if on == 'no':
                return False
            
        else:
            print("Please choose from 'yes' or 'no' ONLY.")

    def show(self):
        print("Speed: ", self.get_speed())
        print("Radius: ", self.__radius)
        print("Is it on?: ", self.__on)
        print("Color: ", self.__color)
    

f1 = Fan()

f1.show()
print('\n')
f1.set_speed('FAST')
print("Speed: ", f1.get_speed())