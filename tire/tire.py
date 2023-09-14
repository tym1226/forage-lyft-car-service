from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, tire_type, tire_wear):
        self.tire_type = tire_type  # Either "Carrigan" or "Octoprime"
        self.tire_wear = tire_wear  # List of four numbers between 0 and 1 representing tire wear

    @abstractmethod
    def needs_service(self):
        if self.tire_type == "Carrigan":
            # Check if any tire wear value is greater than or equal to 0.9
            for wear_level in self.tire_wear:
                if wear_level >= 0.9:
                    return True
            return False
        elif self.tire_type == "Octoprime":
            # Calculate the sum of tire wear levels
            sum_of_wear = sum(self.tire_wear)
            return sum_of_wear >= 3
