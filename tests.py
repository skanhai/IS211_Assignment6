from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)

def test_convertCelsiusToKelvin():
    print("Testing Celsius To Kelvin :")
    test_cases = [0, 25, 50, 100, -10]
    for celsius in test_cases:
        kelvin = convertCelsiusToKelvin(celsius)
        print(f"{celsius:.2f} °C is {kelvin:.2f} K")
    print()

def test_convertCelsiusToFahrenheit():
    print("Testing Celsius To Fahrenheit :")
    test_cases = [0, 25, 50, 100, -10]
    for celsius in test_cases:
        fahrenheit = convertCelsiusToFahrenheit(celsius)
        print(f"{celsius:.2f} °C is {fahrenheit:.2f} °F")
    print()

def test_convertFahrenheitToCelsius():
    print("Testing Fahrenheit To Celsius :")
    test_cases = [32, 68, 86, 122, -4]
    for fahrenheit in test_cases:
        celsius = convertFahrenheitToCelsius(fahrenheit)
        print(f"{fahrenheit:.2f} °F is {celsius:.2f} °C")
    print()

def test_convertFahrenheitToKelvin():
    print("Testing Fahrenheit To Kelvin :")
    test_cases = [32, 68, 86, 122, -4]
    for fahrenheit in test_cases:
        kelvin = convertFahrenheitToKelvin(fahrenheit)
        print(f"{fahrenheit:.2f} °F is {kelvin:.2f} K")
    print()

def test_convertKelvinToCelsius():
    print("Testing Kelvin To Celsius :")
    test_cases = [273.15, 298.15, 323.15, 373.15, 200]
    for kelvin in test_cases:
        celsius = convertKelvinToCelsius(kelvin)
        print(f"{kelvin:.2f} K is {celsius:.2f} °C")
    print()

def test_convertKelvinToFahrenheit():
    print("Testing Kelvin To Fahrenheit: ")
    test_cases = [273.15, 298.15, 323.15, 373.15, 200]
    for kelvin in test_cases:
        fahrenheit = convertKelvinToFahrenheit(kelvin)
        print(f"{kelvin:.2f} K is {fahrenheit:.2f} °F")
    print()


test_convertCelsiusToKelvin()
test_convertCelsiusToFahrenheit()
test_convertFahrenheitToCelsius()
test_convertFahrenheitToKelvin()
test_convertKelvinToCelsius()
test_convertKelvinToFahrenheit()

