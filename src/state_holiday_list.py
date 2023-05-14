from datetime import date
from holidays import *

year = int(input("Enter in the year that you want holidays from: "))

for date, name in sorted(US(subdiv='CA', years=year).items()): # Replace CA with your own state code
    print(date, name)