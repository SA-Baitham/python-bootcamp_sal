#!/usr/bin/env python
import datetime


def age(age=str(input("Enter your date of birth in the format yyyy.mm.dd: "))) -> str:
    age = age.split(".")
    year, month, day = int(age[0]), int(age[1]), int(age[2])
    dob = datetime.datetime(year, month, day)
    # dob = datetime.datetime(dob[0],dob[1],dob[2])
    print("Age Now")
    print("............................................")
    age = datetime.datetime.now() - dob
    print(f"age in days\t: {age.days} \t\tdays ")
    print(f"age in seconds\t: {age.total_seconds()} \tseconds")
    age_in_years = age / datetime.timedelta(days=365.25)
    print(f"age in years\t: {age_in_years} \tyears")


if __name__ == "__main__":
    age()
