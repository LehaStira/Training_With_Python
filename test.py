import csv
import os


CSV_FILENAME = 'obiznaniy/coursera_week3_cars.csv'


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying


    def get_photo_file_ext(self, photo_file_name):
        photo_file_ext = os.path.splitext(photo_file_name)
        return photo_file_ext


class Car(CarBase):
    def __init__(self, car_type, brand, passengers_seats_count, photo_file_name, carrying):
        if isinstance(car_type, str):
            if isinstance(brand, str):
                if isinstance(passengers_seats_count, int):
                    if isinstance(carrying, (float, int)):
                        super().__init__(car_type, brand, photo_file_name, carrying)
                        self.passengers_seats_count = passengers_seats_count
        else:
            ValueError


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        if isinstance(car_type, str):
            if isinstance(brand, str):
                if isinstance(body_whl, str):
                    if isinstance(carrying, (float, int)):
                        super().__init__(car_type, brand, photo_file_name, carrying)
                        self.body_whl = body_whl
                        self.body_height = body_height
                        self.body_width = body_width
                        self.body_length = body_length
        else:
            ValueError


    def get_splitted_body_whl(self):
        body_whl_split = self.body_whl.split('x')
        splitted_body_whl = []
        splitted_body_whl.append(body_whl_split[0])
        splitted_body_whl.append(body_whl_split[1])
        splitted_body_whl.append(body_whl_split[2])
        return splitted_body_whl

    def check_validation_for_body_whl(self):
        new_splitted_body_whl = self.get_splitted_body_whl()
        if (new_splitted_body_whl[0] == 0 or new_splitted_body_whl[1] == 0 or new_splitted_body_whl[2] == 0
                or new_splitted_body_whl[0].isdigit != True or new_splitted_body_whl[1].isdigit != True or
                new_splitted_body_whl[2].isdigit != True):
            flag = 1
        else:
            flag = 0

        return flag

    def get_body_volume(self):
        new_splitted_body_whl = self.get_splitted_body_whl()
        validation_for_body_whl = self.check_validation_for_body_whl()
        body_volume = 0
        if validation_for_body_whl == 1:
            self.body_length = new_splitted_body_whl[0]
            self.body_width = new_splitted_body_whl[1]
            self.body_height = new_splitted_body_whl[2]
            body_volume = float(self.body_length) * float(self.body_width) * float(self.body_height)
        else:
            print("Invalid parameters")

        return body_volume


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        if isinstance(car_type, str):
            if isinstance(brand, str):
                if isinstance(extra, str):
                    if isinstance(carrying, (float, int)):
                        self.extra = extra
                        super().__init__(car_type, brand, photo_file_name, carrying)

        else:
            ValueError('ТУТ ДОЛЖЕН БЫТЬ ТЕКСТ!!!!')




def get_car_list(csv_filename):
    car_list = []
    row_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            row_list.append(row)
        print(row_list)
    for row in row_list:
        for i in range(len(row) // len(row_list)):
            if row[0] == 'car':
                try:
                    new_car = Car(car_type=row[0],
                                  brand=row[1],
                                  passengers_seats_count=row[2],
                                  photo_file_name=row[3],
                                  carrying=row[4])
                except ValueError as err:
                    print("Car type or brand is not STRING!")
                car_list.append(new_car)

            elif row[0] == 'truck':
                try:
                    new_car = Truck(car_type=row[0],
                                    brand=row[1],
                                    photo_file_name=row[2],
                                    carrying=row[3],
                                    body_whl=row[4])
                except ValueError as err:
                    print("Car type or brand is not STRING!")
                except ValueError as err:
                    print("Carrying is not FLOAT")

            elif row[0] == 'spec_machine':
                try:
                    new_car = SpecMachine(car_type=[0],
                                          brand=row[1],
                                          photo_file_name=row[2],
                                          carrying=row[3],
                                          extra=row[4])
                except ValueError as err:
                    print("Car type or brand or extra is not STRING!")
                except ValueError as err:
                    print("Carrying is not FLOAT!")
            else:
                continue
            car_list.append(new_car)
    return car_list


def main():
    new_car_list = get_car_list(CSV_FILENAME)
    print(new_car_list)
    print(Truck.get_body_volume(new_car_list[2]))


if __name__ == "__main__":
    main()

