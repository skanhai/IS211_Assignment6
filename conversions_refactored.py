class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    conversion_table = {
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Celsius", "Fahrenheit"): lambda x: x * 9/5 + 32,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda x: (x + 459.67) * 5/9,
        ("Kelvin", "Fahrenheit"): lambda x: x * 9/5 - 459.67,
        ("Miles", "Yards"): lambda x: x * 1760,
        ("Yards", "Miles"): lambda x: x / 1760,
        ("Miles", "Meters"): lambda x: x * 1609.34,
        ("Meters", "Miles"): lambda x: x / 1609.34,
        ("Yards", "Meters"): lambda x: x * 0.9144,
        ("Meters", "Yards"): lambda x: x / 0.9144
    }

    if fromUnit == toUnit:
        return value

    if (fromUnit, toUnit) in conversion_table:
        return conversion_table[(fromUnit, toUnit)](value)
    else:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not possible")

# Perform tests as specified
print("1. Checking that all temperature conversions are working...")
print("Converting 0 Celsius to Kelvin:", convert("Celsius", "Kelvin", 0))
print("Converting 273.15 Kelvin to Celsius:", convert("Kelvin", "Celsius", 273.15))
print("Converting 0 Celsius to Fahrenheit:", convert("Celsius", "Fahrenheit", 0))
print("Converting 32 Fahrenheit to Celsius:", convert("Fahrenheit", "Celsius", 32))
print("Converting 32 Fahrenheit to Kelvin:", convert("Fahrenheit", "Kelvin", 32))
print("Converting 273.15 Kelvin to Fahrenheit:", convert("Kelvin", "Fahrenheit", 273.15))

print("\n2. Checking that all distance conversions are working...")
print("Converting 1 Mile to Yards:", convert("Miles", "Yards", 1))
print("Converting 1760 Yards to Miles:", convert("Yards", "Miles", 1760))
print("Converting 1 Mile to Meters:", convert("Miles", "Meters", 1))
print("Converting 1609.34 Meters to Miles:", convert("Meters", "Miles", 1609.34))
print("Converting 1 Yard to Meters:", convert("Yards", "Meters", 1))
print("Converting 0.9144 Meters to Yards:", convert("Meters", "Yards", 0.9144))

print("\n3. Checking that converting from one unit to itself returns the same value for all units...")
print("Converting 100 Celsius to Celsius:", convert("Celsius", "Celsius", 100))
print("Converting 10 Miles to Miles:", convert("Miles", "Miles", 10))

print("\n4. Checking that converting from incompatible units raises a ConversionNotPossible exception...")
try:
    print("Attempting to convert 100 Celsius to Miles.")
    convert("Celsius", "Miles", 100)
except ConversionNotPossible as y:
    print("ConversionNotPossible exception raised:", y)
