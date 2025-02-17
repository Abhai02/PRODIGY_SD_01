def convert_temperature(value, unit):
    if unit == "C":
        kelvin = value + 273.15
        fahrenheit = (value * 1.8) + 32
        print(f"{value:.2f}°C = {kelvin:.2f}K = {fahrenheit:.2f}°F")
    elif unit == "K":
        celsius = value - 273.15
        fahrenheit = (value - 273.15) * 1.8 + 32
        print(f"{value:.2f}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")
    elif unit == "F":
        celsius = (value - 32) * 5/9
        kelvin = (value - 32) * 5/9 + 273.15
        print(f"{value:.2f}°F = {celsius:.2f}°C = {kelvin:.2f}K")
    else:
        print("Invalid unit. Please enter C, K, or F.")

def main():
    print("Welcome to the Temperature Conversion Program!")
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C for Celsius, K for Kelvin, F for Fahrenheit): ").strip().upper()
        convert_temperature(value, unit)
    except ValueError:
        print("Invalid input! Please enter a valid numeric temperature.")

if __name__ == "__main__":
    main()
