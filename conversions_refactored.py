class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    if fromUnit == toUnit:
        return value

    if (fromUnit, toUnit) in [("Celsius", "Kelvin"), ("Kelvin", "Celsius"),
                              ("Celsius", "Fahrenheit"), ("Fahrenheit", "Celsius"),
                              ("Fahrenheit", "Kelvin"), ("Kelvin", "Fahrenheit")]:
        if fromUnit == "Celsius" and toUnit == "Kelvin":
            return value + 273.15
        elif fromUnit == "Kelvin" and toUnit == "Celsius":
            return value - 273.15
        elif fromUnit == "Celsius" and toUnit == "Fahrenheit":
            return value * 9/5 + 32
        elif fromUnit == "Fahrenheit" and toUnit == "Celsius":
            return (value - 32) * 5/9
        elif fromUnit == "Fahrenheit" and toUnit == "Kelvin":
            return (value + 459.67) * 5/9
        elif fromUnit == "Kelvin" and toUnit == "Fahrenheit":
            return value * 9/5 - 459.67

    elif (fromUnit, toUnit) in [("Miles", "Yards"), ("Yards", "Miles"),
                                ("Miles", "Meters"), ("Meters", "Miles"),
                                ("Yards", "Meters"), ("Meters", "Yards")]:
        if fromUnit == "Miles" and toUnit == "Yards":
            return value * 1760
        elif fromUnit == "Yards" and toUnit == "Miles":
            return value / 1760
        elif fromUnit == "Miles" and toUnit == "Meters":
            return value * 1609.34
        elif fromUnit == "Meters" and toUnit == "Miles":
            return value / 1609.34
        elif fromUnit == "Yards" and toUnit == "Meters":
            return value * 0.9144
        elif fromUnit == "Meters" and toUnit == "Yards":
            return value / 0.9144

    else:
        raise ConversionNotPossible("Conversion from {} to {} is not possible".format(fromUnit, toUnit))


print("1. Checking that all temperature conversions are working.")
print("Converting 0 Celsius to Kelvin:", convert("Celsius", "Kelvin", 0))
print("Converting 273.15 Kelvin to Celsius:", convert("Kelvin", "Celsius", 273.15))
print("Converting 0 Celsius to Fahrenheit:", convert("Celsius", "Fahrenheit", 0))
print("Converting 32 Fahrenheit to Celsius:", convert("Fahrenheit", "Celsius", 32))
print("Converting 32 Fahrenheit to Kelvin:", convert("Fahrenheit", "Kelvin", 32))
print("Converting 273.15 Kelvin to Fahrenheit:", convert("Kelvin", "Fahrenheit", 273.15))

print("\n2. Checking that all distance conversions are working.")
print("Converting 1 Mile to Yards:", convert("Miles", "Yards", 1))
print("Converting 1760 Yards to Miles:", convert("Yards", "Miles", 1760))
print("Converting 1 Mile to Meters:", convert("Miles", "Meters", 1))
print("Converting 1609.34 Meters to Miles:", convert("Meters", "Miles", 1609.34))
print("Converting 1 Yard to Meters:", convert("Yards", "Meters", 1))
print("Converting 0.9144 Meters to Yards:", convert("Meters", "Yards", 0.9144))

print("\n3. Checking that converting from one unit to itself returns the same value for all units.")
print("Converting 100 Celsius to Celsius:", convert("Celsius", "Celsius", 100))
print("Converting 10 Miles to Miles:", convert("Miles", "Miles", 10))

print("\n4. Checking that converting from incompatible units raises a ConversionNotPossible exception.")
try:
    print("Attempting to convert 100 Celsius to Miles.")
    convert("Celsius", "Miles", 100)
except ConversionNotPossible as x:
    print("ConversionNotPossible exception raised:", x)

