class Car:
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    
    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed
    
    def accelerate(self):
        self.__speed = int(self.__speed) + 5
        print("Accelerate to: ", self.__speed, "Kilometers per hour")
        return self.__speed
    
    def brake(self):
        self.__speed = int(self.__speed) - 5
        print("Brake to: ", self.__speed, "Kilometers per hour")
        return self.__speed
    
    def show(self):
        print("Year Model: ", self.__year_model)
        print("Make: ", self.__make)
        print("Current Speed: ", self.__speed, "Kilometers per second")
    

