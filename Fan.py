class fan:
    def __init__(self, fan_speed = 1, radius = 5, color = 'blue', on = False):
        self.__fan_speed = int(fan_speed)
        self.__radius = float(radius)
        self.__on = bool(on)
        self.__color = str(color)

