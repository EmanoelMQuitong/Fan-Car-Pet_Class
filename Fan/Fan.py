class Fan:
    def __init__(self, speed, radius, color, on):
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
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        if radius >= 5.0 or radius <= 10.0:
            self.__radius = float(radius)
        
        else:
            print("Please choose from '5.0' to '10.0' ONLY.")

    def get_on(self):
        return self.__on
    
    def set_on(self, on):
        on = on.lower()
        if on == 'yes' or on == 'no':
            if on == 'yes':
                self.__on = True
            if on == 'no':
                self.__on = False
            
        else:
            print("Please choose from 'yes' or 'no' ONLY.")
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color.lower()

    def show(self):
        print("Speed: ", self.get_speed())
        print("Radius: ", self.get_radius())
        print("Is it on?: ", self.get_on())
        print("Color: ", self.get_color())
    

f1 = Fan('slow', '5.76', 'no', 'fuisha')

f1.show()
print('\n')
f1.set_speed('FAST')
print("Speed: ", f1.get_speed())