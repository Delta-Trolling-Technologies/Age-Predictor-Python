#!/usr/bin/env python3
# You should remove these text with the hashtags in front of them
# No brain = no gain
from datetime import datetime, date
print("Enter your birthdate (yyyy mm dd)")
date_of_birth = datetime.strptime(input(":"), "%Y %m %d")
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
age = calculate_age(date_of_birth)
print("Your age is: ", age)
