# Define global conversion factors with NO spaces
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Get user input
temperature_input = input("Enter the temperature to convert: ")

try:
    temperature = float(temperature_input)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "F":
    celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {celsius}°C")
elif unit == "C":
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {fahrenheit}°F")
else:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
