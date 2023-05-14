from datetime import date
from holidays import *

year = int(input("Enter in the year that you want holidays from: "))

north_america = CA(years=year) + US(years=year) + MX(years=year)

print(north_america)