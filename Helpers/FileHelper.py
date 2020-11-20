import os
import csv


class FileHelper:

    def __init__(self):
        self.__helpers_directory = os.path.dirname(__file__)
        self.__main_directory = os.path.dirname(self.__helpers_directory)
        self.__data_directory = os.path.join(self.__main_directory, 'Data')
        self.__models_directory = os.path.join(self.__main_directory, 'Models')

    def save_vehicle(self, vehicle):
        path = f'{self.__data_directory}/Vehicle.csv'

        new_vehicle = [
            self.__get_next_id(path),
            vehicle.get_name(),
            vehicle.get_year(),
            vehicle.get_make(),
            vehicle.get_model(),
            vehicle.get_color()
        ]

        with open(path, 'a', newline='') as file:
            file_writer = csv.writer(file)
            file_writer.writerow(new_vehicle)

        return

    def delete_vehicle(self, vehicle_id):
        original_path = f'{self.__data_directory}/Vehicle.csv'
        updated_path = f'{self.__data_directory}/Vehicle_updated.csv'
        self.__delete_file_entry(vehicle_id, original_path, updated_path)
        return

    def save_gas_entry(self, entry):
        path = f'{self.__data_directory}/GasEntry.csv'

        new_entry = [
            self.__get_next_id(path),
            entry.get_vehicle_id(),
            entry.get_date(),
            entry.get_odometer(),
            entry.get_quantity(),
            entry.get_price_per_gallon()
        ]

        with open(path, 'a', newline='') as file:
            file_writer = csv.writer(file)
            file_writer.writerow(new_entry)

        return

    def delete_gas_entry(self, entry_id):
        old_path = f'{self.__data_directory}/GasEntry.csv'
        updated_path = f'{self.__data_directory}/GasEntry_updated.csv'
        self.__delete_file_entry(entry_id, old_path, updated_path)
        return

    @staticmethod
    def __get_next_id(path):
        ids = []

        with open(path, 'r') as file:
            file.readline()  # read first line to get past the header

            while True:
                line = file.readline()
                if not line:
                    break
                ids.append(line.split(',')[0])

        max_id = 0
        if len(ids) > 0:
            max_id = int(max(ids))
        return max_id + 1

    @staticmethod
    def __delete_file_entry(entry_id, original_path, updated_path):
        with open(original_path, 'r') as old_file, open(updated_path, 'w', newline='') as new_file:
            file_writer = csv.writer(new_file)
            # write every line except for the one I want to delete into the new file
            for row in csv.reader(old_file):
                if len(row) < 1:
                    break
                if row[0] != str(entry_id):
                    file_writer.writerow(row)

        # delete the old file
        os.remove(original_path)
        # rename the new file to the old name
        os.rename(updated_path, original_path)
        return
