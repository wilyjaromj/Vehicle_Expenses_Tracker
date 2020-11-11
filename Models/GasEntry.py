import datetime


class GasEntry:

    def __init__(self, vehicle_id, date, odometer, quantity, price_per_gallon, entry_id=0):

        self.__vehicle_id = vehicle_id
        self.__date = date
        self.__odometer = odometer
        self.__quantity = quantity
        self.__price_per_gallon = price_per_gallon
        self.__entry_id = entry_id

    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_id(self, id):
        self.__vehicle_id = id
        return

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date
        return

    def get_odometer(self):
        return self.__odometer

    def set_odometer(self, odometer):
        self.__odometer = odometer
        return

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity
        return

    def get_price_per_gallon(self):
        return self.__price_per_gallon

    def set_price_per_gallon(self, ppg):
        self.__price_per_gallon = ppg
        return

    def get_id(self):
        return self.__entry_id

    def set_id(self, new_id):
        self.__entry_id = new_id
        return
