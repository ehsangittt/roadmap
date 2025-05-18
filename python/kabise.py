def is_leap_year(year):
    if (year % 4 == 3) #or (year % 4 == 0 and year % 100 != 0):
        print("Sal kabise ast.")
    else:
        print("Kabise nist.")
year = int(input("year? "))
is_leap_year(year)
