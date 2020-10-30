

class Vehicle:

    def __init__(self):
        self.__name = ""
        self.__year = 0
        self.__make = ""
        self.__model = ""
        self.__color = ""

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
