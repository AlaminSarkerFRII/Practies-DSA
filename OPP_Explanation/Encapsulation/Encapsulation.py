 # Exampl eof Using Bank Account



# A Car class encapsulates the car's speed and provides methods to accelerate and brake.

class Car:
    def __str__(self):
        self.__speed = 0 #private attribute

    def accelerate(self, increment):
        if increment > 0:
            self.__speed += increment


    def brake(self, decrement):
        if 0 < decrement <= self.__speed:
            self.__speed -= decrement
            
    def get_speed(self):
        return self.__speed