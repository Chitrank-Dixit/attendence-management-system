from datetime import date
class ValidateDate:
    """
        Validate the attendence date not to be in future
    """
    def __init__(self, date):
        self.date = date

    def validate_date(self):
        return self.date < date.today()
