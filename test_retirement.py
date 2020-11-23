import pytest
from pytest_bdd import scenario, scenarios, given, when, then
import FullRetirementAge


scenarios('full_retirement_age.feature')

@scenario(
    "full_retirement_age.feature",
    "The user input birth year that is between 1944 and 1953",
    example_converters=dict(year=int, full_SSA_year=int)
)
def test_outlined():
    pass

@given("The Retirement age calculator is running")
def test_running():
    pass

@when('The user input 1905 for birth year and 5 for birth month')
def test_1905_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1905')
    assert int(input("Enter the year of birth: ")) == 1905

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 65 and 0 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1905)

    assert full_retirement_age[0] == 65
    assert full_retirement_age[1] == 0

@when('The user input 1938 for birth year and 5 for birth month')
def test_1938_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1938')
    assert int(input("Enter the year of birth: ")) == 1938

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 65 and 2 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1938)

    assert full_retirement_age[0] == 65
    assert full_retirement_age[1] == 2

@when('The user input 1939 for birth year and 5 for birth month')
def test_1939_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1939')
    assert int(input("Enter the year of birth: ")) == 1939

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 65 and 4 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1939)

    assert full_retirement_age[0] == 65
    assert full_retirement_age[1] == 4

@when('The user input 1940 for birth year and 5 for birth month')
def test_1940_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1940')
    assert int(input("Enter the year of birth: ")) == 1940

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 65 and 6 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1940)

    assert full_retirement_age[0] == 65
    assert full_retirement_age[1] == 6

@when('The user input 1941 for birth year and 5 for birth month')
def test_1941_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1941')
    assert int(input("Enter the year of birth: ")) == 1941

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 65 and 8 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1941)

    assert full_retirement_age[0] == 65
    assert full_retirement_age[1] == 8

@when('The user input 1942 for birth year and 5 for birth month')
def test_1942_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1942')
    assert int(input("Enter the year of birth: ")) == 1942

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 65 and 10 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1942)

    assert full_retirement_age[0] == 65
    assert full_retirement_age[1] == 10

@when('The user input 1943 for birth year and 5 for birth month')
def test_1943_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1943')
    assert int(input("Enter the year of birth: ")) == 1943

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 66 and 0 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1953)

    assert full_retirement_age[0] == 66
    assert full_retirement_age[1] == 0

@when('The user input 1954 for birth year and 5 for birth month')
def test_1954_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1954')
    assert int(input("Enter the year of birth: ")) == 1954

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 66 and 0 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1954)

    assert full_retirement_age[0] == 66
    assert full_retirement_age[1] == 0

@when('The user input 1955 for birth year and 5 for birth month')
def test_1955_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1955')
    assert int(input("Enter the year of birth: ")) == 1955

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 66 and 2 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1955)

    assert full_retirement_age[0] == 66
    assert full_retirement_age[1] == 2

@when('The user input 1956 for birth year and 5 for birth month')
def test_1956_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1956')
    assert int(input("Enter the year of birth: ")) == 1956

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 66 and 4 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1956)

    assert full_retirement_age[0] == 66
    assert full_retirement_age[1] == 4

@when('The user input 1957 for birth year and 5 for birth month')
def test_1957_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1957')
    assert int(input("Enter the year of birth: ")) == 1957

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 66 and 6 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1957)

    assert full_retirement_age[0] == 66
    assert full_retirement_age[1] == 6

@when('The user input 1958 for birth year and 5 for birth month')
def test_1958_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1958')
    assert int(input("Enter the year of birth: ")) == 1958

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 66 and 8 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1958)

    assert full_retirement_age[0] == 66
    assert full_retirement_age[1] == 8

@when('The user input 1959 for birth year and 5 for birth month')
def test_1959_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1959')
    assert int(input("Enter the year of birth: ")) == 1959

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 66 and 10 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1959)

    assert full_retirement_age[0] == 66
    assert full_retirement_age[1] == 10

@when('The user input 1960 for birth year and 5 for birth month')
def test_1960_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1960')
    assert int(input("Enter the year of birth: ")) == 1960

    monkeypatch.setattr('builtins.input', lambda _:'5')
    assert int(input("Enter the month of birth: ")) == 5

@then('The full retirement age is 67 and 0 months')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1960)

    assert full_retirement_age[0] == 67
    assert full_retirement_age[1] == 0

@when("the user input 3000 for birth year")
def test_3000(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'3000')
    assert int(input("Enter the year of birth: ")) == 3000

@then("the calculator output ValueError about 3000")
def test_calculate_retirement_age(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3000')
    with pytest.raises(ValueError):
        assert FullRetirementAge.user_year() == 3000

@when("the user input 1899 for birth year")
def test_1899(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:'1899')
    assert int(input("Enter the year of birth: ")) == 1899

@then("the calculator output ValueError about 1899")
def test_calculate_retirement_age(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1899')
    with pytest.raises(ValueError):
        assert FullRetirementAge.user_year() == 1899

@when('The user input "<year>" for birth year and 5 for birth month')
@pytest.mark.parametrize("year", [1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953])
def test_between_1944_and_1953(year):
    expected = (year, 5)
    assert year, 5 == expected

@then('the full retirement age is 66 and 0 month')
def test_calculate_retirement_age():
    full_retirement_age = FullRetirementAge.find_year(1950)

    assert full_retirement_age[0] == 66
    assert full_retirement_age[1] == 0
