from battery.battery import Battery

from helpers import subtract_years_from_date

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        new_date = subtract_years_from_date(self.current_date, 2)
        if new_date > self.last_service_date:
            return True
        return False
