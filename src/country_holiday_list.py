from datetime import date
from holidays import *

year = int(input("Enter in the year that you want holidays from: "))

for date, name in sorted(UK(years = year).items()): # Replace UK with your own country code

    print(date, name)