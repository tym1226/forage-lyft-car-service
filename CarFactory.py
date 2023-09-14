from datetime import date
from engine import Engine
from car import Car  # Import the Car class
from engine import CapuletEngine
from engine import WilloughbyEngine
from engine import SternmanEngine
from battery import SplindlerBattery
from battery import NubbinBattery
from tire import Tire

class CarFactory:
    def __init__(self):
        pass

    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, engine, battery, tire_type, tire_wear):
        # Create a Calliope car
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date, current_date)
        tire = Tire(tire_type, tire_wear)
        return Car(engine, battery, tire)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, engine, battery, tire_type, tire_wear):
        # Create a Glissade car
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date, current_date)
        tire = Tire(tire_type, tire_wear)
        return Car(engine, battery, tire)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool, engine, battery, tire_type, tire_wear):
        # Create a Palindrome car
        engine = SternmanEngine(last_service_date, warning_light_on)
        battery = SplindlerBattery(last_service_date, current_date)
        tire = Tire(tire_type, tire_wear)
        return Car(engine, battery, tire)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, engine, battery, tire_type, tire_wear):
        # Create a Rorschach car
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Tire(tire_type, tire_wear)
        return Car(engine, battery, tire)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, engine, battery, tire_type, tire_wear):
        # Create a Thovex car
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Tire(tire_type, tire_wear)
        return Car(engine, battery, tire)
