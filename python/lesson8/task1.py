import datetime


date_format = '%d-%m-%Y'


class Date:
    def __init__(self, date_text=None, day=None, month=None, year=None):
        if date_text is None:
            self.day = day
            self.month = month
            self.year = year
        else:
            parsed_date = datetime.datetime.strptime(date_text, date_format)
            self.day = parsed_date.day
            self.month = parsed_date.month
            self.year = parsed_date.year

    def __str__(self):
        return f"day = {self.day}, month = {self.month}, year = {self.year}"

    @staticmethod
    def validate(date_text):
        try:
            datetime.datetime.strptime(date_text, date_format)
            print("Valid date")
        except ValueError:
            print("Invalid date")

    @classmethod
    def parse(cls, date_text):
        parsed_date = datetime.datetime.strptime(date_text, date_format)
        return cls(day=parsed_date.day, month=parsed_date.month, year=parsed_date.year)


Date.validate("01-02-2013")
Date.validate("01-13-2013")

print(Date(date_text="01-02-2013"))
print(Date.parse("05-01-2010"))
