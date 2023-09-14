from datetime import date
from engine import Engine
from car import Car  # Import the Car class
from engine import CapuletEngine
from engine import WilloughbyEngine
from engine import SternmanEngine
from battery import SplindlerBattery
from battery import NubbinBattery

class CarFactory:
    def __init__(self):
        pass

    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, engine, battery):
        # Create a Calliope car
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, engine, battery):
        # Create a Glissade car
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool, engine, battery):
        # Create a Palindrome car
        engine = SternmanEngine(last_service_date, warning_light_on)
        battery = SplindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, engine, battery):
        # Create a Rorschach car
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, engine, battery):
        # Create a Thovex car
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
