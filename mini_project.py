def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

start_year = int(input("Enter The Starting Year: "))
end_year = int(input("Enter The Ending Year: "))
leap_years = []

for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        leap_years.append(year)

print(f"\nLeap years between {start_year} and {end_year}:")
print(leap_years)
print(f"\nTotal Number of Leap Years: {len(leap_years)}")
