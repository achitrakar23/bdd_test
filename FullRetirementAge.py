def calculator(year, month):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    retirement_age, retirement_month = find_year(year)
    full_ssa_month = (retirement_month + month) % 12
    full_ssa_year = retirement_age + year

    if full_ssa_month > 12:
        full_ssa_month -= 12
        full_ssa_year += 1

    print("Your full retirement age is", retirement_age, "and", retirement_month, "months")
    print("This date will be in", months[full_ssa_month - 1], "of", full_ssa_year)
def find_year(year):
    retirement_age = 0
    retirement_month = 0

    if year <= 1937:
        return [65, 0]
    elif year == 1938:
        return [65, 2]
    elif year == 1939:
        return [65, 4]
    elif year == 1940:
        return [65, 6]
    elif year == 1941:
        return [65, 8]
    elif year == 1942:
        return [65, 10]
    elif year == 1943 or year <= 1954:
        return [66, 0]
    elif year == 1955:
        return [66, 2]
    elif year == 1956:
        return [66, 4]
    elif year == 1957:
        return [66, 6]
    elif year == 1958:
        return [66, 8]
    elif year == 1959:
        return [66, 10]
    elif year >= 1960:
        return [67, 0]

    return retirement_age, retirement_month
def user_year():

    user_input_year = int(input("Enter the year of birth: "))

    if user_input_year < 1900:
        raise ValueError
    elif user_input_year >= 3000:
        raise ValueError

    return user_input_year

def user_month():

    user_input_month = int(input("Enter the month of birth: "))

    if user_input_month < 1 or user_input_month > 12:
        raise ValueError

    return user_input_month

def main():
    print("Social Security Full Retirement Age Calculator")
    print()

    input_year = user_year()
    input_month = user_month()
    calculator(input_year, input_month)


if __name__ == '__main__':
    main()

