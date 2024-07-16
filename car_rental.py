# %%
import datetime

class CarRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        return f"We have currently {self.stock} cars available to rent."

    def rent_car_hourly(self, n):
        if n <= 0:
            return "Number of cars should be positive!"
        elif n > self.stock:
            return "Sorry, we have currently {} cars available to rent.".format(self.stock)
        else:
            self.stock -= n
            now = datetime.datetime.now()
            return now

    def rent_car_daily(self, n):
        if n <= 0:
            return "Number of cars should be positive!"
        elif n > self.stock:
            return "Sorry, we have currently {} cars available to rent.".format(self.stock)
        else:
            self.stock -= n
            now = datetime.datetime.now()
            return now

    def rent_car_weekly(self, n):
        if n <= 0:
            return "Number of cars should be positive!"
        elif n > self.stock:
            return "Sorry, we have currently {} cars available to rent.".format(self.stock)
        else:
            self.stock -= n
            now = datetime.datetime.now()
            return now

    def return_car(self, request):
        rental_time, rental_basis, num_of_cars = request
        bill = 0

        if rental_time and rental_basis and num_of_cars:
            self.stock += num_of_cars
            now = datetime.datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:  # hourly
                bill = round(rental_period.seconds / 3600) * 5 * num_of_cars
            elif rental_basis == 2:  # daily
                bill = round(rental_period.days) * 20 * num_of_cars
            elif rental_basis == 3:  # weekly
                bill = round(rental_period.days / 7) * 60 * num_of_cars

            return bill
        else:
            return "Are you sure you rented a car with us?"


# %%
class Customer:
    def __init__(self):
        self.cars = 0
        self.rental_basis = 0
        self.rental_time = 0

    def request_car(self):
        cars = input("How many cars would you like to rent?")
        try:
            cars = int(cars)
        except ValueError:
            print("Number of cars should be a positive integer!")
            return -1
        if cars < 1:
            print("Number of cars should be greater than zero!")
            return -1
        else:
            self.cars = cars
        return self.cars

    def return_car(self):
        if self.rental_basis and self.rental_time and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return 0, 0, 0
