# Online-Car-Rental-using-Python
This project implements a car rental system using Python, featuring a main  module and classes for managing car rentals and customer interactions. The  system allows customers to rent cars on an hourly, daily, or weekly basis and  provides functionalities for returning cars and calculating rental bills. 
# MODULES AND CLASSES 
1. CarRental Class
   Attributes: 
        o stock: Tracks the number of cars available for rent. 
   Methods: 
        o __init__(stock=0): Initializes the car rental shop with a specified stock of cars. 
        o display_stock(): Returns the current number of cars available for rent. 
        o rent_car_hourly(n): Rents n cars on an hourly basis. Updates the stock and returns the rental time. 
        o rent_car_daily(n): Rents n cars on a daily basis. Updates the stock and returns the rental time. 
        o rent_car_weekly(n): Rents n cars on a weekly basis. Updates the stock and returns the rental time. 
        o return_car(request): Processes the return of cars, calculates the bill based on the rental duration and type, and updates the stock. 
2.  Customer Class
    Attributes: 
        o cars: Number of cars the customer wants to rent. 
        o rental_basis: Indicates the rental basis (hourly, daily and weekly). 
        o rental_time: Records the time of rental. 
    Methods: 
        o __init__(): Initializes customer attributes. 
        o request_car(): Prompts the customer for the number of cars they wish to rent. Validates input. 
        o return_car(): Returns the customer's rental details for processing. 
3.  # MAIN APPLICATION
4.  The car_rental_main.ipynb file serves as the user interface, presenting options to display available cars, rent cars on various bases, return cars, and exit the system.
      Features: 
           Menu Options: 
                1. Display available cars. 
                2. Rent cars on an hourly basis. 
                3. Rent cars on a daily basis. 
                4. Rent cars on a weekly basis. 
                5. Return cars and calculate the bill. 
                6. Exit the application. 
           Workflow: 
                o Users interact with a menu to choose actions. 
                o Validations ensure correct input and sufficient stock before renting. 
                o Upon returning cars, the system calculates the bill based on the rental period and type. 
5.  # CONCLUSION 
6. This car rental system provides a comprehensive solution for managing car rentals, allowing for flexible rental durations and straightforward billing. The modular design using Object-Oriented Programming principles makes it easy to maintain and extend. 
      
   
