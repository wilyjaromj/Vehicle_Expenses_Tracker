

class Vehicle:

    def __init__(self, name, year, make, model, color, vehicle_id=0):
        self.__name = name
        self.__year = year
        self.__make = make
        self.__model = model
        self.__color = color
        self.__vehicle_id = vehicle_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year
        return

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make
        return

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model
        return

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
        return

    def get_id(self):
        return self.__vehicle_id

    def set_id(self, new_id):
        self.__color = new_id
        return
