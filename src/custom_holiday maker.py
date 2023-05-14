from datetime import date
from holidays import *

class CustomHolidays():
    
    def _fill(self, year):

        UK._populate(self, year)

        self.pop_named("Boxing Day") # Remove any amount of holidays with pop_named()

        self[date(year, 1, 1)] = "NetFruit Technologies Day" # Add any amount of holidays with self[date(year, month, day)]