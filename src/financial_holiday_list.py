from datetime import date
from holidays import *

year = int(input("Enter in the year that you want holidays from: "))

for date, name in sorted(financial_holidays(market = 'NYSE', years = year).items()): # Replace NYSE with your own financial market code

    print(date, name)