from abc import ABC

from car import Car

from datetime import timedelta

from battery import Battery

class SplindlerBattery(Car, Battery, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        service_limit = timedelta(days=365 * 3)
        return self.current_date - self.last_service_date > service_limit
