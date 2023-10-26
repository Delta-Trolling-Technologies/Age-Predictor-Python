#!/usr/bin/env python3
# Predict age with brain
# No brain = no gain
from datetime import datetime, date
print("Enter ur birthdate (yyyy mm dd)")
date_of_birth = datetime.strptime(input(":"), "%Y %m %d")
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
age = calculate_age(date_of_birth)
print("Ur age is: ", age)