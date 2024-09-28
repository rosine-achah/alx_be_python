FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    converted_value = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return converted_value


def convert_to_fahrenheit(celsius):
    converted_value =  (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return converted_value


def main():
    try: 
        temperature  = float(input("Enter the temperature to convert:"))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
        if unit  == "C":
           converted = convert_to_fahrenheit(temperature)
           print(f"{temperature}°C is {converted} °F")
    
        elif unit == "F":
           converted = convert_to_celsius(temperature)
           print(f"{temperature}°F is {converted} °C")
        else:
           print("Invalid temperature. Please enter a numeric value")
     except Valueerror:
           print(“Invalid temperature. Please enter a numeric value.”)

if __name__ == "__main__":
    main()
