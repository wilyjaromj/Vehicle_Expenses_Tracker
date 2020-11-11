import os


class FileHelper:

    def __init__(self):
        self.__helpers_directory = os.path.dirname(__file__)
        self.__main_directory = os.path.dirname(self.__helpers_directory)
        self.__data_directory = os.path.join(self.__main_directory, 'Data')
        self.__models_directory = os.path.join(self.__main_directory, 'Models')

    def save_vehicle(self, vehicle):
        path = f'{self.__data_directory}/Vehicle.csv'
        vehicle_info = f'\n{self.__get_next_id(path)},{vehicle.get_name()},{vehicle.get_year()},' \
                       f'{vehicle.get_make()},{vehicle.get_model()},{vehicle.get_color()}'

        file = open(path, 'a')
        file.write(vehicle_info)
        file.close()
        return

    def save_gas_entry(self, entry):
        path = f'{self.__data_directory}/GasEntry.csv'
        entry_info = f'\n{self.__get_next_id(path)},{entry.get_vehicle_id()},{entry.get_date()},' \
                     f'{entry.get_odometer()},{entry.get_quantity()},{entry.get_price_per_gallon()}'

        file = open(path, 'a')
        file.write(entry_info)
        file.close()
        return

    @staticmethod
    def __get_next_id(path):
        ids = []
        file = open(path, 'r')
        file.readline()  # read first line to get past the header

        while True:
            line = file.readline()
            if not line:
                break
            ids.append(line.split(',')[0])

        file.close()
        max_id = 0
        if len(ids) > 0:
            max_id = int(max(ids))
        return max_id + 1
