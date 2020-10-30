import datetime


class GasEntry:

    def __init__(self, vehicle_id):
        self.__vehicle_id = vehicle_id
        self.__date = datetime.date.today()
        self.__odometer = 0
        self.__quantity = 0
        self.__price_per_gallon = 0

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_odometer(self):
        return self.__odometer

    def set_odometer(self, odometer):
        self.__odometer = odometer

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_price_per_gallon(self):
        return self.__price_per_gallon

    def set_price_per_gallon(self, ppg):
        self.__price_per_gallon = ppg
