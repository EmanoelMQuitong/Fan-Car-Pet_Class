class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        name = name.upper()
        self.__name = name
    
    def set_animal_type(self, animal_type):
        animal_type = animal_type.upper()
        self.__animal_type = animal_type

    def set_age(self, age):
        age = int(age)
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
    def show(self):
        print("Animal name: ", self.__name)
        print("Animal Type: ", self.__animal_type)
        print("Age: ", self.__age, "months")

