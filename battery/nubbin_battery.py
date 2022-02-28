from battery import Battery

from dateutil.relativedelta import relativedelta

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        year_difference = relativedelta(current_date, last_service_date).years
        if year_difference > 4:
            return True
        return False
