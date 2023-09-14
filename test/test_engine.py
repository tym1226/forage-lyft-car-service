import unittest
from datetime import datetime
from engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine

class TestEngine(unittest.TestCase):
    def test_needs_service_abstract(self):
        # Attempt to create an instance of the abstract base class Engine
        with self.assertRaises(TypeError):
            engine = Engine(datetime(2020, 1, 1))

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        # Create a CapuletEngine instance with last_service_mileage
        last_service_date = datetime(2020, 1, 1)
        current_mileage = 50000  # Exceeds 30000 miles threshold
        last_service_mileage = 20000
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)

        # Test that the CapuletEngine needs service
        self.assertTrue(engine.needs_service())

        # Test that the CapuletEngine doesn't need service
        current_mileage = 25000
        engine.current_mileage = current_mileage
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        # Create a SternmanEngine instance with warning_light_is_on
        last_service_date = datetime(2020, 1, 1)
        warning_light_on = True  # Warning light is on
        engine = SternmanEngine(last_service_date, warning_light_on)

        # Test that the SternmanEngine needs service when the warning light is on
        self.assertTrue(engine.needs_service())

        # Test that the SternmanEngine doesn't need service when the warning light is off
        warning_light_on = False
        engine.warning_light_is_on = warning_light_on
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        # Create a WilloughbyEngine instance with last_service_mileage
        last_service_date = datetime(2020, 1, 1)
        current_mileage = 70000  # Exceeds 60000 miles threshold
        last_service_mileage = 40000
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)

        # Test that the WilloughbyEngine needs service
        self.assertTrue(engine.needs_service())

        # Test that the WilloughbyEngine doesn't need service
        current_mileage = 55000
        engine.current_mileage = current_mileage
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
