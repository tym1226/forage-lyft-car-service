import unittest
from datetime import datetime, timedelta
from battery import Battery, NubbinBattery, SplindlerBattery
import sys
sys.path.append('/Users/yumengtao/Documents/Workspace/Forage/forage-lyft-starter-repo/battery')

class TestBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        # Create a Battery instance with a last_service_date
        last_service_date = datetime(2020, 1, 1)
        battery = Battery(last_service_date)

        # Test that the battery needs service
        current_date = datetime(2024, 1, 1)
        self.assertTrue(battery.needs_service(current_date))

        # Test that the battery doesn't need service
        current_date = datetime(2022, 1, 1)
        self.assertFalse(battery.needs_service(current_date))

    def test_nubbin_battery_needs_service(self):
        # Create a NubbinBattery instance with last_service_date
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2024, 1, 1)
        nubbin_battery = NubbinBattery(last_service_date, current_date)

        # Test that the NubbinBattery needs service (service_limit is 4 years)
        self.assertTrue(nubbin_battery.needs_service())

        # Test that the NubbinBattery doesn't need service
        current_date = datetime(2022, 1, 1)
        nubbin_battery.current_date = current_date
        self.assertFalse(nubbin_battery.needs_service())

    def test_splindler_battery_needs_service(self):
        # Create a SplindlerBattery instance with last_service_date
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2024, 1, 1)
        splindler_battery = SplindlerBattery(last_service_date, current_date)

        # Test that the SplindlerBattery needs service (service_limit is 2 years)
        self.assertTrue(splindler_battery.needs_service())

        # Test that the SplindlerBattery doesn't need service
        current_date = datetime(2022, 1, 1)
        splindler_battery.current_date = current_date
        self.assertFalse(splindler_battery.needs_service())

if __name__ == '__main__':
    unittest.main()
